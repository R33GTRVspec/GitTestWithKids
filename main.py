import sys
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelationalTableModel
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox, \
    QTableView
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
#some text

# в этом классе создадим модель нашего приложения
class MainWindow(QDialog):
    # про *args и **kwargs можно почитать тут https://habr.com/ru/company/ruvds/blog/482464/
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("OurSchoolDiaryUi.ui", self)

        # установим текущую дату
        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        # Зададим параметры для tableWidget
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(4, 110)
        self.tableWidget.setColumnWidth(5, 110)
        self.tableWidget.setRowCount(50)

        # Загрузим данные в таблицу
        self.tableView_loaddata()

        # добавляем данные, сгенерированные созданными функциями
        self.comboBox_students.addItems(self.populate_students_from_students_table())
        self.comboBox_subject.addItems(self.populate_lessons_from_lessons_table())
        self.comboBox_grade.addItems(self.populate_grades_from_grades_table())
        self.comboBox_zachto.addItems(self.populate_jobtypes_from_jobtypes_table())

        # проверим, что там в комбобоксах
        print(self.save_current_values_in_comboboxes())

        # поажимаем единственный пашбаттон и повыываем какую-нибудь функцию с печатью в консоль
        #        self.pb_writeToDB(self.btnstate())

        # поажимаем более осознанно на единственный пашбаттон и дернем функцию записи в БД
        self.pb_writeToDB.clicked.connect(self.eventSaving)
        self.pb_writeToDB.clicked.connect(self.tableView_loaddata)

        # Create a connection to the SQLite database
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('databases/OurSchoolDiary.sqlite')
        if not self.db.open():
            self.label.setText("Нет связи с базой данных")
        else:
            self.label.setText("База данных подключена")
            # Create a model to display the data in the TableView

    # Функция для загрузки в окно программы сведений из таблицы событий в БД
    def tableView_loaddata(self):
        db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных
        cnn = sqlite3.connect(db_name)
        c = cnn.cursor()
        sqlquery = """
        SELECT  Event_id AS "ID", Date AS "Дата",
        (SELECT StudentName FROM Students WHERE Student_id = Events.Student) AS "Ученик",
        (SELECT Lesson FROM Lessons WHERE Lesson_id = Events.Lesson) AS "Предмет",
        (SELECT Grade FROM Grades WHERE Grade_id = Events.Grade) AS "Оценка",
        (SELECT JobTypeName FROM JobTypes WHERE JobType_ID = Events.JobType) AS "Тип задания"
        FROM
        Events
        LIMIT 50
        """
        result = c.execute(sqlquery)
        tablerow = 0
        for row in result:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    # задаем путь и имя к нашей базе данных
    db_name = 'databases/OurSchoolDiary.sqlite'

    # запасная функция для подключения к базе данных
    # def connect_db(db_name):
    #     db = QSqlDatabase.addDatabase(
    #         'QSQLITE')  # Переменная для определения драйвера типа базы данных. В нашем случае это QSQLITE
    #     db.setDatabaseName(db_name)  # Переменная которую мы получаем на вход для этой функции
    #     if not db.open():  # Проверка на подключение. Выведет в консоль ошибку и выйдет из приложения, если не подключится
    #         print('Нет соединения с базой данных!')
    #         sys.exit()
    #         return False

    # Создадим функции, которые заполняют комбобоксы значениями из соответствующих таблиц в БД
    # Для студентов. Возвращает строку со списком значений
    def populate_students_from_students_table(self):
        db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных
        cnn = sqlite3.connect(db_name)
        c = cnn.cursor()
        c.execute("SELECT StudentName FROM Students")
        list_of_strings = [item[0] for item in c.fetchall()]
        cnn.commit()
        cnn.close()
        print(list_of_strings)
        return list_of_strings

    # Для предметов. Возвращает строку со списком значений
    def populate_lessons_from_lessons_table(self):
        db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных
        cnn = sqlite3.connect(db_name)
        c = cnn.cursor()
        c.execute("SELECT Lesson FROM Lessons")
        list_of_strings = [item[0] for item in c.fetchall()]
        cnn.commit()
        cnn.close()
        print(list_of_strings)
        return list_of_strings

    # Для оценок. Возвращает строку со списком значений
    def populate_grades_from_grades_table(self):
        db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных
        cnn = sqlite3.connect(db_name)
        c = cnn.cursor()
        c.execute("SELECT Grade FROM Grades")
        list_of_strings = [item[0] for item in c.fetchall()]
        cnn.commit()
        cnn.close()
        print(list_of_strings)
        return list_of_strings

    # Для типов работы за что оценка. Возвращает строку со списком значений
    def populate_jobtypes_from_jobtypes_table(self):
        db_name = 'databases/OurSchoolDiary.sqlite'
        cnn = sqlite3.connect(db_name)
        c = cnn.cursor()
        c.execute("SELECT JobTypeName FROM JobTypes")
        list_of_strings = [item[0] for item in c.fetchall()]
        cnn.commit()
        cnn.close()
        print(list_of_strings)
        return list_of_strings

    # Создадим функцию, которая будет записывать текущие значения в комбобоксах в переменную
    def save_current_values_in_comboboxes(self):
        # создаем список в порядке ('Ученик', 'Предмет', 'Оценка', 'Тип задания')
        current_comboboxes_values = (
            (self.comboBox_students.currentText()), (self.comboBox_subject.currentText()),
            (self.comboBox_grade.currentText()),
            (self.comboBox_zachto.currentText()))
        return current_comboboxes_values

    # Создадим функцию для записи выбранных значений в базу данных
    def eventSaving(self):
        # Создаем отдельные переменные с текущими значениями из комбобоксов
        student = self.comboBox_students.currentText()
        subject = self.comboBox_subject.currentText()
        grade = self.comboBox_grade.currentText()
        zachto = self.comboBox_zachto.currentText()
        date = self.dateEdit.date().toString("dd-MM-yyyy")

        # создаем переменную-контейнер для написания запросов
        query = QSqlQuery()

        # подготовка ID нужного нам объекта для записи в таблицу
        # студенты
        query.prepare("SELECT Student_id FROM Students WHERE StudentName=:student")
        query.bindValue(":student", student)
        query.exec()
        query.first()
        student_id = query.value(0)
        # предмет
        query.prepare("SELECT Lesson_id FROM Lessons WHERE Lesson=:subject")
        query.bindValue(":subject", subject)
        query.exec()
        query.next()
        subject_id = query.value(0)
        # оценка
        query.prepare("SELECT Grade_id FROM Grades WHERE Grade=:grade")
        query.bindValue(":grade", grade)
        query.exec()
        query.next()
        grade_id = query.value(0)
        # за что
        query.prepare("SELECT JobType_ID FROM JobTypes WHERE JobTypeName=:zachto")
        query.bindValue(":zachto", zachto)
        query.exec()
        query.next()
        zachto_id = query.value(0)

        # Вставляем Значения в таблицу Events, используя первичные ключи из дочерних таблиц в качестве внешних ключей
        query.prepare(
            "INSERT INTO Events (Date, Student, Lesson, Grade, JobType) VALUES ( :date, :student, :subject, :grade, :zachto)")
        query.bindValue(":date", date)
        query.bindValue(":student", student_id)
        query.bindValue(":subject", subject_id)
        query.bindValue(":grade", grade_id)
        query.bindValue(":zachto", zachto_id)
        query.exec()
        query.finish()

        # Проверим, получилось ли записать данные
        if query.lastError().isValid():
            # если LastError выполненный для нашего query вернул хоть какую-то ошибку, то isValid вернет True и тогда:
            self.label.setText("Не могу сохранить данные")
        else:
            # если LastError не вернул никаких ошибок, то isValid вернет False и тогда:
            self.label.setText("Данные сохранены")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
