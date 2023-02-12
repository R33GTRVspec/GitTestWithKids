# Our perfect school app
#
# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow
# from ui_mainwindow import Ui_MainWindow
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = MainWindow()
#     window.show()
#
#     sys.exit(app.exec())

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import *

Form, Window = uic.loadUiType('OurSchoolDiaryUi.ui')

db_name = 'databases/OurSchoolDiary.sqlite'  # задаем путь и имя к нашей базе данных


# напишем функцию для подключенмия к базе данных
def connect_db(db_name):
    db = QSqlDatabase.addDatabase('QSQLITE')  # переменная для определения типа базы данных. В нашем случае это QSQLITE
    db.setDatabaseName(db_name)  # переменная которую мы получаем в этой функции
    if not db.open():
        print('Нет соединения с базой данных')
        return False


if not connect_db(db_name):
    sys.exit(-1)
else:
    print('Соединение установлено.')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
