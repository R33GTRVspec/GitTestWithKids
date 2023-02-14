# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OurSchoolDiaryUi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.line_1 = QFrame(MainWindow)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(20, 10, 600, 16))
        self.line_1.setLineWidth(2)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(MainWindow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 450, 600, 20))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.comboBox_zachto = QComboBox(MainWindow)
        self.comboBox_zachto.setObjectName(u"comboBox_zachto")
        self.comboBox_zachto.setGeometry(QRect(170, 200, 200, 28))
        font = QFont()
        font.setPointSize(15)
        self.comboBox_zachto.setFont(font)
        self.label_student = QLabel(MainWindow)
        self.label_student.setObjectName(u"label_student")
        self.label_student.setGeometry(QRect(30, 82, 81, 20))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label_student.setFont(font1)
        self.comboBox_students = QComboBox(MainWindow)
        self.comboBox_students.setObjectName(u"comboBox_students")
        self.comboBox_students.setGeometry(QRect(170, 80, 200, 28))
        self.comboBox_students.setFont(font)
        self.label_subject = QLabel(MainWindow)
        self.label_subject.setObjectName(u"label_subject")
        self.label_subject.setGeometry(QRect(30, 122, 101, 20))
        self.label_subject.setFont(font1)
        self.comboBox_subject = QComboBox(MainWindow)
        self.comboBox_subject.setObjectName(u"comboBox_subject")
        self.comboBox_subject.setGeometry(QRect(170, 120, 200, 28))
        self.comboBox_subject.setFont(font)
        self.label_zachto = QLabel(MainWindow)
        self.label_zachto.setObjectName(u"label_zachto")
        self.label_zachto.setGeometry(QRect(30, 202, 135, 20))
        self.label_zachto.setFont(font1)
        self.label_date = QLabel(MainWindow)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(30, 33, 61, 41))
        self.label_date.setFont(font1)
        self.label_grade = QLabel(MainWindow)
        self.label_grade.setObjectName(u"label_grade")
        self.label_grade.setGeometry(QRect(30, 161, 100, 21))
        self.label_grade.setFont(font1)
        self.comboBox_grade = QComboBox(MainWindow)
        self.comboBox_grade.setObjectName(u"comboBox_grade")
        self.comboBox_grade.setGeometry(QRect(170, 160, 200, 28))
        self.comboBox_grade.setFont(font)
        self.pb_writeToDB = QPushButton(MainWindow)
        self.pb_writeToDB.setObjectName(u"pb_writeToDB")
        self.pb_writeToDB.setGeometry(QRect(400, 90, 201, 81))
        font2 = QFont()
        font2.setPointSize(22)
        self.pb_writeToDB.setFont(font2)
        self.pb_writeToDB.setStyleSheet(u"background-color: rgb(253, 142, 15);")
        self.pb_writeToDB.setCheckable(False)
        self.line_2 = QFrame(MainWindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 240, 600, 20))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.tableView = QTableView(MainWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 264, 600, 181))
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.horizontalHeader().setDefaultSectionSize(90)
        self.dateEdit = QDateEdit(MainWindow)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(170, 40, 200, 28))
        self.dateEdit.setFont(font)
        self.dateEdit.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QDate(2023, 1, 1))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u043f\u043e \u0443\u0441\u043f\u0435\u0432\u0430\u0435\u043c\u043e\u0441\u0442\u0438", None))
        self.label_student.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a:", None))
        self.label_subject.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442:", None))
        self.label_zachto.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u043d\u0438\u044f:", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.label_grade.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0446\u0435\u043d\u043a\u0430:", None))
        self.pb_writeToDB.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u0411\u0414", None))
    # retranslateUi

