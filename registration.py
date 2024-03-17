from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from database import DB

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
from kodik import Ui_MainWindowt as kodikk

import random
import os

load_dotenv()

def resource_path(relative_path):
    try:
        path = (sys._MEIPASS + '\\' + relative_path).replace('\\', '/')
    except Exception:
        path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/' + relative_path

    return path

# Генерация случайного шестизначного кода
def generate_confirmation_code():
    return ''.join(random.choices('0123456789', k=6)) # делает 6-ти значный код с числами от 0 до 9

confirmation_code = generate_confirmation_code()

class Ui_MainWindow_reg(object):
    def setupUi(self, MainWindow_reg):
        MainWindow_reg.setObjectName("MainWindow_reg")
        MainWindow_reg.resize(340, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{resource_path('vk.jpg')}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_reg.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow_reg)
        self.centralwidget.setObjectName("centralwidget")
        self.label_reg = QtWidgets.QLabel(self.centralwidget)
        self.label_reg.setGeometry(QtCore.QRect(100, 20, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_reg.setFont(font)
        self.label_reg.setStyleSheet("")
        self.label_reg.setObjectName("label_reg")
        self.pochta = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pochta.setGeometry(QtCore.QRect(60, 80, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pochta.setFont(font)
        self.pochta.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.pochta.setObjectName("pochta")
        self.label_pocht = QtWidgets.QLabel(self.centralwidget)
        self.label_pocht.setGeometry(QtCore.QRect(60, 50, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_pocht.setFont(font)
        self.label_pocht.setObjectName("label_pocht")
        self.password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(60, 220, 180, 30))
        self.password.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.password.setObjectName("password")
        self.login = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(60, 150, 180, 30))
        self.login.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.login.setObjectName("login")
        self.powtor_password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.powtor_password.setGeometry(QtCore.QRect(60, 300, 180, 30))
        self.powtor_password.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.powtor_password.setObjectName("powtor_password")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(60, 120, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_log.setFont(font)
        self.label_log.setObjectName("label_log")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(60, 190, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_powt_password = QtWidgets.QLabel(self.centralwidget)
        self.label_powt_password.setGeometry(QtCore.QRect(60, 270, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_powt_password.setFont(font)
        self.label_powt_password.setObjectName("label_powt_password")
        self.galochka = QtWidgets.QCheckBox(self.centralwidget)
        self.galochka.setGeometry(QtCore.QRect(60, 340, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.galochka.setFont(font)
        self.galochka.setObjectName("galochka")
        self.registr = QtWidgets.QPushButton(self.centralwidget)
        self.registr.setGeometry(QtCore.QRect(60, 370, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.registr.setFont(font)
        self.registr.setStyleSheet("QPushButton {\n"
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
        self.registr.setObjectName("registr")
        self.est_account = QtWidgets.QPushButton(self.centralwidget)
        self.est_account.setGeometry(QtCore.QRect(100, 430, 110, 20))
        self.est_account.setStyleSheet("QPushButton {\n"
"    color:  rgb(0, 85, 255);\n"
"    border: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #bfbfbf;\n"
"}")
        self.est_account.setObjectName("est_account")
        MainWindow_reg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_reg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_reg.setMenuBar(self.menubar)

        self.registr.clicked.connect(self.gal)

        self.retranslateUi(MainWindow_reg)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_reg)

    def retranslateUi(self, MainWindow_reg):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_reg.setWindowTitle(_translate("MainWindow_reg", "Registration"))
        self.label_reg.setText(_translate("MainWindow_reg", "Регистрация"))
        self.label_pocht.setText(_translate("MainWindow_reg", "почта"))
        self.label_log.setText(_translate("MainWindow_reg", "логин"))
        self.label_password.setText(_translate("MainWindow_reg", "пароль"))
        self.label_powt_password.setText(_translate("MainWindow_reg", "повторите пароль"))
        self.galochka.setText(_translate("MainWindow_reg", "Я согласен на обработку персональных данных"))
        self.registr.setText(_translate("MainWindow_reg", "Зарегистрироваться"))
        self.est_account.setText(_translate("MainWindow_reg", "уже есть аккаунт"))

    def gal(self):
            if self.galochka.isChecked():
                self.zaregistr()
            else:
                self.negal()

    def negal(self):
            zareg = QMessageBox()
            zareg.setWindowTitle("Программа")
            zareg.setText("Подтвердите соглашение персональных данных!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()


    def zaregistr(self):
        zareg = QMessageBox()
        zareg.setWindowTitle("Программа")

        # если не все окна заполнены
        if not all([self.pochta.toPlainText(), self.login.toPlainText(), self.password.toPlainText(), self.powtor_password.toPlainText()]):

            zareg.setText("Заполните окна регистрации!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            return

        elif self.password.toPlainText() != self.powtor_password.toPlainText():

            zareg.setText("Пароли не совпадают!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            return

        user = DB().execute('SELECT * FROM users WHERE email = %s', (self.pochta.toPlainText(),))
        user = user.fetchall()
        if user:
            zareg.setText("Данная почта уже существует, введите другую почту!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            return

        user = DB().execute('SELECT * FROM users WHERE login = %s', (self.login.toPlainText(),))
        user = user.fetchall()
        if user:
            zareg.setText("Данный логин уже занят, введите другое имя!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            return

        self.email()

    def email(self):
        sender_email = os.getenv("EMAIL_USERNAME")
        sender_password = os.getenv("app_password")

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = self.pochta.toPlainText()
        message["Subject"] = "Код подтверждения"

        message_body = f"Ваш код подтверждения: {confirmation_code}"

        message.attach(MIMEText(message_body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, self.pochta.toPlainText(), message.as_string())
                self.kot.show()

        except Exception as e:
            zareg = QMessageBox()
            zareg.setWindowTitle("Программа")
            zareg.setText("Данной почты не существует, введите существующую почту!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            return None

        return confirmation_code

class Kot(QtWidgets.QMainWindow, kodikk):
    def __init__(self, regUI, *args, **kwargs):
            self.regUI = regUI

            QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
            self.ui = kodikk()
            self.ui.setupUi(self)


            self.ui.next.clicked.connect(self.ok)

    def ok(self):
        zareg = QMessageBox()
        zareg.setWindowTitle("Программа")

        if self.ui.kod.toPlainText() == confirmation_code:
            pochta = self.regUI.pochta.toPlainText()
            login = self.regUI.login.toPlainText()
            password = self.regUI.password.toPlainText()

            self.regUI.pochta.clear()
            self.regUI.login.clear()
            self.regUI.password.clear()
            self.regUI.powtor_password.clear()

            if all([pochta, login, password]):
                DB().execute("INSERT INTO users (email, login, password) VALUES (%s, %s, %s)", (pochta, login, password))

            zareg.setText("Вы успешно зарегистрировались!")
            zareg.setIcon(QMessageBox.Information)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zamok.png')}"))

            zareg.exec_()
            self.close()
        else:
            zareg.setText("Код введен неверно!")
            zareg.setIcon(QMessageBox.Warning)
            zareg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            zareg.setWindowIcon(QIcon(f"{resource_path('zak.jpg')}"))

            zareg.exec_()
        self.ui.kod.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow_reg()
    MainWindow_reg = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow_reg)
    MainWindow_reg.show()

    ui.kot = Kot(ui)

    sys.exit(app.exec_())