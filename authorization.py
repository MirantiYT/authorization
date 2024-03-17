from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

import os

from database import DB

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID() # что бы выставить аватарку у приложения

from registration import Kot, Ui_MainWindow_reg

def resource_path(relative_path):
    try:
        path = (sys._MEIPASS + '\\' + relative_path).replace('\\', '/')
    except Exception:
        path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/' + relative_path

    return path

class Ui_MainWindow_avt(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 325)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{resource_path('sec.png')}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parol_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.parol_text.setGeometry(QtCore.QRect(80, 170, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.parol_text.setFont(font)
        self.parol_text.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.parol_text.setObjectName("parol_text")
        self.login_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.login_text.setGeometry(QtCore.QRect(80, 100, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.login_text.setObjectName("login_text")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(80, 70, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.label_parol = QtWidgets.QLabel(self.centralwidget)
        self.label_parol.setGeometry(QtCore.QRect(80, 140, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_parol.setFont(font)
        self.label_parol.setObjectName("label_parol")
        self.label_auto = QtWidgets.QLabel(self.centralwidget)
        self.label_auto.setGeometry(QtCore.QRect(110, 20, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_auto.setFont(font)
        self.label_auto.setStyleSheet("")
        self.label_auto.setObjectName("label_auto")
        self.vhod = QtWidgets.QPushButton(self.centralwidget)
        self.vhod.setGeometry(QtCore.QRect(70, 220, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vhod.setFont(font)
        self.vhod.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: white;\n"
"    border: 2px rgb(0, 85, 255);\n"
"    padding: 10px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #bfbfbf;\n"
"}")
        self.vhod.setObjectName("vhod")
        self.net_account = QtWidgets.QPushButton(self.centralwidget)
        self.net_account.setGeometry(QtCore.QRect(120, 280, 110, 20))
        self.net_account.setStyleSheet("QPushButton {\n"
"    color:  rgb(0, 85, 255);\n"
"    border: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #bfbfbf;\n"
"}")
        self.net_account.setObjectName("net_account")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.net_account.clicked.connect(self.knopcka)

        self.vhod.clicked.connect(self.click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_login.setText(_translate("MainWindow", "логин"))
        self.label_parol.setText(_translate("MainWindow", "пароль"))
        self.label_auto.setText(_translate("MainWindow", "Авторизация"))
        self.vhod.setText(_translate("MainWindow", "Вход"))
        self.net_account.setText(_translate("MainWindow", "Зарегистрироваться"))

    def knopcka(self):
        MainWindow.close()
        reg.show()

    def click(self):
            if not all([self.login_text.toPlainText(), self.parol_text.toPlainText()]):
                zareg = QMessageBox()
                zareg.setWindowTitle("Программа")
                zareg.setText("Введите логин и пароль!")
                zareg.setIcon(QMessageBox.Warning)
                zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

                zareg.exec_()
            else:
                user = DB().execute('SELECT * FROM users WHERE (email = %s OR login = %s) AND password = %s', (self.login_text.toPlainText(), self.login_text.toPlainText(), self.parol_text.toPlainText()))
                user = user.fetchall()
                if user:
                    zareg = QMessageBox()
                    zareg.setWindowTitle("Программа")
                    zareg.setText("Вы успешно вошли!")
                    zareg.setIcon(QMessageBox.Information)
                    zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

                    zareg.exec_()
                else:
                    zareg = QMessageBox()
                    zareg.setWindowTitle("Программа")
                    zareg.setText("Неверный логин или пароль! Попробуйте снова!")
                    zareg.setIcon(QMessageBox.Warning)
                    zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    zareg.setWindowIcon(QIcon(f"{resource_path('zak.jpg')}"))

                    zareg.exec_()

class Reg(QtWidgets.QMainWindow, Ui_MainWindow_reg):
    def __init__(self, *args, **kwargs):
            QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
            self.ui = Ui_MainWindow_reg()
            self.ui.setupUi(self)
            self.ui.kot = Kot(self.ui)
            self.ui.est_account.clicked.connect(self.ch)

    def ch(self):
        self.close()
        MainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow_avt()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    reg = Reg()

    sys.exit(app.exec_())