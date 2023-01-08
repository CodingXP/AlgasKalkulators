import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import load_ui


FIXED_WIDTH = 860
FIXED_HEIGHT = 720



class HomeWindow(QDialog):
    def __init__(self):
        super(HomeWindow,self).__init__()
        uic.loadUi("home.ui", self)
        self.Register.clicked.connect(self.goToReg)
        self.Login.clicked.connect(self.goToLog)
        self.Quit.clicked.connect(self.quit)

    def goToReg(self):
        register = RegisterWindow()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToLog(self):
        login = LoginWindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def quit(self):
        sys.exit()



class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi("login.ui", self)
        self.logButton.clicked.connect(self.loginUser)
        self.regButton.clicked.connect(self.goToReg)
        self.menuButton.clicked.connect(self.goToMenu)

    def loginUser(self):
        email = self.email.text()
        if self.password.text() == self.cPassword.text():
            password = self.password.text()
            print("Login Successful, email:" + email + ", password: " + password)
        else:
            print("Incorrect password!")
    
    def goToReg(self):
        register = RegisterWindow()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)


class RegisterWindow(QDialog):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        uic.loadUi("register.ui",self)
        self.regButton.clicked.connect(self.reigsterUser)
        self.logButton.clicked.connect(self.goToLog)
        self.menuButton.clicked.connect(self.goToMenu)

    def goToLog(self):
        login = LoginWindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def reigsterUser(self):
        name = self.name.text()
        surname = self.surname.text()
        email = self.email.text()
        if self.password.text() == self.cPassword.text():
            password = self.password.text()
            print("Registered Successfully! Welcome, " + name + " " + surname)
        else:
            print("Passwords do not match!")


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
homewindow = HomeWindow()
widget.addWidget(homewindow)

widget.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")
