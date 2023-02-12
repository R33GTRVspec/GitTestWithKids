
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import *

Form, Window = uic.loadUiType('OurSchoolDiaryUi.ui')

db_name = 'OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных


# напишем функцию для подключенмия к базе данных
def connect_db(db_name):
    db = QSqlDatabase.addDatabase('QSQLITE')    # переменная для определения типа базы данных. В нашем случае это QSQLITE
    db.setDatabaseName(db_name)                 # переменная которую мы получаем на вход для этой функции
    if not db.open():                           # проверка на подключение. Выведет в консоль ошибку и выйдет из приложения, если не подключится
        print('Нет соединения с базой данных!')
        sys.exit()
        return False



connect_db(db_name)         # подключимся к нашей базе данных


Events = QSqlTableModel()   #   Мы создали переменную Events (по имени нашей таблицы с событиями), использовали объект класса QSqlTableModel или "модель таблицы".
                            #   Эту переменную мы будем использовать ниже для заполнения объекта tableView - form.tableView.setModel(Events)
Events.setTable('Events')   #   Сказали, что привязываем к созданному выше объекту таблицу с именем "Events"
Events.select()             #   Далее выполняем простой селект, вытаскивая все строки

# привяжем к первому комбобоксу Информацию из таблицы Students


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.tableView.setSortingEnabled(True) # разрешаем сортировку столбцов для нашего tableView
form.tableView.setModel(Events)


window.show()
app.exec()
