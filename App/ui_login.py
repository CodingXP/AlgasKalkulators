# Form implementation generated from reading ui file 'c:\Users\visti\Desktop\Project\AlgasKalkulators\App\login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(860, 720)
        Dialog.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 80, 101, 41))
        self.label.setStyleSheet("color: rgb(255, 246, 230);\n"
"font: 28pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(250, 210, 361, 31))
        self.email.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Rockwell\";")
        self.email.setObjectName("email")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 180, 51, 21))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(340, 300, 181, 31))
        self.password.setStyleSheet("font: 8pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 260, 71, 21))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(370, 350, 131, 21))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.cPassword = QtWidgets.QLineEdit(Dialog)
        self.cPassword.setGeometry(QtCore.QRect(340, 390, 181, 31))
        self.cPassword.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Rockwell\";")
        self.cPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.cPassword.setObjectName("cPassword")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(340, 690, 201, 20))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.logButton = QtWidgets.QPushButton(Dialog)
        self.logButton.setGeometry(QtCore.QRect(360, 440, 151, 41))
        self.logButton.setStyleSheet("font: 14pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.logButton.setObjectName("logButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 530, 391, 21))
        self.label_2.setStyleSheet("color: rgb(255, 246, 230);\n"
"font: 15pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.regButton = QtWidgets.QPushButton(Dialog)
        self.regButton.setGeometry(QtCore.QRect(600, 530, 75, 23))
        self.regButton.setStyleSheet("font: 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.regButton.setObjectName("regButton")
        self.home = QtWidgets.QPushButton(Dialog)
        self.home.setGeometry(QtCore.QRect(360, 590, 151, 41))
        self.home.setStyleSheet("font: 14pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.home.setObjectName("home")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "E-mail"))
        self.label_5.setText(_translate("Dialog", "Password"))
        self.label_6.setText(_translate("Dialog", "Confirm Password"))
        self.label_7.setText(_translate("Dialog", "Made by DP3-2 PIKC RVT || 2023"))
        self.logButton.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "If you do not have an account, sign up here:"))
        self.regButton.setText(_translate("Dialog", "Register"))
        self.home.setText(_translate("Dialog", "Home"))
