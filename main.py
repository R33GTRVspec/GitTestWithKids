import sys
import sqlite3
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import *
from PyQt6.QtCore import QDate, QDateTime, QTime, Qt

Form, Window = uic.loadUiType('OurSchoolDiaryUi.ui')

db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных


# напишем функцию для подключения к базе данных
def connect_db(db_name):
    db = QSqlDatabase.addDatabase(
        'QSQLITE')  # Переменная для определения драйвера типа базы данных. В нашем случае это QSQLITE
    db.setDatabaseName(db_name)  # Переменная которую мы получаем на вход для этой функции
    if not db.open():  # Проверка на подключение. Выведет в консоль ошибку и выйдет из приложения, если не подключится
        print('Нет соединения с базой данных!')
        sys.exit()
        return False


# заполним комбобоксы и окно для данных информацией без принципов ООП

connect_db(db_name)  # подключимся к нашей базе данных

# Далее заполним пустую область 'tableView'(название объекта из Дизайнера) для таблицы данными
Events = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
print(Events)
#   Эту переменную мы будем использовать ниже для заполнения объекта tableView - form.tableView.setModel(Events)
Events.setTable('Events')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Events"
Events.select()  # Далее выполняем простой селект, вытаскивая все строки


# Всякие тесты с текущей датой/временем
# now = QDate.currentDate()
# print(now.toString(Qt.DateFormat.ISODate))
# print(now.toString(Qt.DateFormat.RFC2822Date))
# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
# time = QTime.currentTime()
# print(time.toString(Qt.DateFormat.ISODate))

# Попытка реализовать принципы ООП


# Создадим функции, которые заполняют комбобоксы "Ученик", "Предмет", "Оценка за" и
# "Оценка" значениями из соответствующих таблиц в БД

# Для студентов. Возвращает строку со списком значений
def populate_students_from_students_table():
    cnn = sqlite3.connect(db_name)
    c = cnn.cursor()
    c.execute("SELECT Student FROM Students")
    list_of_strings = [item[0] for item in c.fetchall()]
    cnn.commit()
    cnn.close()
    print(list_of_strings)
    return list_of_strings


# Для предметов. Возвращает строку со списком значений
def populate_lessons_from_lessons_table():
    cnn = sqlite3.connect(db_name)
    c = cnn.cursor()
    c.execute("SELECT Lesson FROM Lessons")
    list_of_strings = [item[0] for item in c.fetchall()]
    cnn.commit()
    cnn.close()
    print(list_of_strings)
    return list_of_strings


# Для оценок. Возвращает строку со списком значений
def populate_grades_from_grades_table():
    cnn = sqlite3.connect(db_name)
    c = cnn.cursor()
    c.execute("SELECT Grade FROM Grades")
    list_of_strings = [item[0] for item in c.fetchall()]
    cnn.commit()
    cnn.close()
    print(list_of_strings)
    return list_of_strings


# Для типов работы за что оценка. Возвращает строку со списком значений
def populate_jobtypes_from_jobtypes_table():
    cnn = sqlite3.connect(db_name)
    c = cnn.cursor()
    c.execute("SELECT JobTypeName FROM JobTypes")
    list_of_strings = [item[0] for item in c.fetchall()]
    cnn.commit()
    cnn.close()
    print(list_of_strings)
    return list_of_strings


# Создадим функцию, которая будет записывать текущие значения в комбобоксах в переменную
def save_current_values_in_comboboxes():
    # создаем список в порядке ('Ученик', 'Предмет', 'Оценка', 'Тип задания')
    current_comboboxes_values = (
    (form.comboBox_students.currentText()), (form.comboBox_subject.currentText()), (form.comboBox_grade.currentText()),
    (form.comboBox_zachto.currentText()))
    return current_comboboxes_values

# def refresh_current_combobox_values(self):
#     button = QPushButton('Toggle Me')
#     button.setCheckable(True)
#     button.clicked.connect(self.on_toggle)

# def on_toggle(self.checked):
#     print(checked)


def update(self):
    save_current_values_in_comboboxes()
    print(save_current_values_in_comboboxes())


app = QApplication([])
w = Window()
form = Form()
form.setupUi(w)

# разрешаем сортировку столбцов для нашего tableView
form.tableView.setSortingEnabled(True)

# берем данные выше, над функциями, пока топорно, надо переделать на Функцию
form.tableView.setModel(Events)

# добавляем данные, сгенерированные созданными выше функциями
form.comboBox_students.addItems(populate_students_from_students_table())
form.comboBox_subject.addItems(populate_lessons_from_lessons_table())
form.comboBox_grade.addItems(populate_grades_from_grades_table())
form.comboBox_zachto.addItems(populate_jobtypes_from_jobtypes_table())

# установим текущую дату
form.dateEdit.setDateTime(QDateTime.currentDateTime())

# просто проверим, что функция записи значений из комбобоксов сделала список нужных нам данных
print(save_current_values_in_comboboxes())

# просто проверяем, что мы умеем отслеживать нажатие кнопки
button_update = QtWidgets.QPushButton('pb_writeToDB')
if button_update.clicked.connect(self.on):
    update()
    print(save_current_values_in_comboboxes())
else:
    print('not saved')

w.show()
app.exec()
