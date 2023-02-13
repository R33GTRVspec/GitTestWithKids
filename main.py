import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import *
from PyQt6.QtCore import QDate, QDateTime, QTime, Qt

import sqlite3

Form, Window = uic.loadUiType('OurSchoolDiaryUi.ui')

db_name = 'OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных


# напишем функцию для подключенмия к базе данных
def connect_db(db_name):
    db = QSqlDatabase.addDatabase('QSQLITE')  # переменная для определения типа базы данных. В нашем случае это QSQLITE
    db.setDatabaseName(db_name)  # переменная которую мы получаем на вход для этой функции
    if not db.open():  # проверка на подключение. Выведет в консоль ошибку и выйдет из приложения, если не подключится
        print('Нет соединения с базой данных!')
        sys.exit()
        return False


# заполним комбобоксы и окно для данных информацией без принципов ООП

connect_db(db_name)  # подключимся к нашей базе данных

# Далее заполним пустую область 'tableView'(название объекта из Дизайнера) для таблицы данными
Events = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
#   Эту переменную мы будем использовать ниже для заполнения объекта tableView - form.tableView.setModel(Events)
Events.setTable('Events')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Events"
Events.select()  # Далее выполняем простой селект, вытаскивая все строки

# привяжем к первому комбобоксу Информацию из таблицы Students
Students = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект
# класса QSqlTableModel или "модель таблицы". Эту переменную мы будем использовать ниже для заполнения комбобокса выбора студентов
Students.setTable('Students')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Students"
Students.select()  # Далее выполняем простой селект, вытаскивая все строки


# привяжем ко второму комбобоксу Информацию из таблицы Lessons
Lessons = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
#   Эту переменную мы будем использовать ниже для заполнения комбобокса выбора предмета
Lessons.setTable('Lessons')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Lessons"
Lessons.select()  # Далее выполняем простой селект, вытаскивая все строки

# привяжем ко второму комбобоксу Информацию из таблицы Lessons
Grades = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
#   Эту переменную мы будем использовать ниже для заполнения комбобокса выбора предмета
Grades.setTable('Grades')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Lessons"
Grades.select()  # Далее выполняем простой селект, вытаскивая все строки

# привяжем ко второму комбобоксу Информацию из таблицы Lessons
JobTypes = QSqlTableModel()  # Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
#   Эту переменную мы будем использовать ниже для заполнения комбобокса выбора предмета
JobTypes.setTable('JobTypes')  # Сказали, что привязываем к созданному выше объекту таблицу с именем "Lessons"
JobTypes.select()  # Далее выполняем простой селект, вытаскивая все строки

# Всякие тесты с текущей датой/временем
# now = QDate.currentDate()
# print(now.toString(Qt.DateFormat.ISODate))
# print(now.toString(Qt.DateFormat.RFC2822Date))
# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
# time = QTime.currentTime()
# print(time.toString(Qt.DateFormat.ISODate))


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.tableView.setSortingEnabled(True)  # разрешаем сортировку столбцов для нашего tableView
form.tableView.setModel(Events)
form.comboBox_students.setModel(Students)
form.comboBox_subject.setModel(Lessons)
form.comboBox_grade.setModel(Grades)
form.comboBox_zachto.setModel(JobTypes)
form.dateEdit.setDateTime(QDateTime.currentDateTime())

window.show()
app.exec()
