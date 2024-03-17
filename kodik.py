from PyQt5 import QtCore, QtGui, QtWidgets
import os

def resource_path(relative_path):
    try:
        path = (sys._MEIPASS + '\\' + relative_path).replace('\\', '/')
    except Exception:
        path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/' + relative_path

    return path

class Ui_MainWindowt(object):
    def setupUi(self, MainWindowt):
        MainWindowt.setObjectName("MainWindowt")
        MainWindowt.resize(310, 175)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{resource_path('zak.jpg')}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowt.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindowt)
        self.centralwidget.setObjectName("centralwidget")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(120, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setStyleSheet("QPushButton {\n"
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
        self.next.setObjectName("next")
        self.kodtext = QtWidgets.QLabel(self.centralwidget)
        self.kodtext.setGeometry(QtCore.QRect(90, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.kodtext.setFont(font)
        self.kodtext.setObjectName("kodtext")
        self.kod = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kod.setGeometry(QtCore.QRect(70, 50, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.kod.setFont(font)
        self.kod.setStyleSheet("padding: 2px;  border-radius: 10px; border: 2px rgb(191, 191, 191); background-color: rgb(191, 191, 191);")
        self.kod.setObjectName("kod")
        MainWindowt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
        self.menubar.setObjectName("menubar")
        MainWindowt.setMenuBar(self.menubar)

        self.retranslateUi(MainWindowt)
        QtCore.QMetaObject.connectSlotsByName(MainWindowt)

    def retranslateUi(self, MainWindowt):
        _translate = QtCore.QCoreApplication.translate
        MainWindowt.setWindowTitle(_translate("MainWindowt", "MainWindow"))
        self.next.setText(_translate("MainWindowt", "OK"))
        self.kodtext.setText(_translate("MainWindowt", "введите 6-значный код"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowt = QtWidgets.QMainWindow()
    ui = Ui_MainWindowt()
    ui.setupUi(MainWindowt)
    MainWindowt.show()
    sys.exit(app.exec_())
