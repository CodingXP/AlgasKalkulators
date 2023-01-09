import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox  


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
        self.home.clicked.connect(self.goToMenu)
        self.setWindowTitle("Login")

    def loginUser(self):
        try:
            email = self.email.text()
            if self.password.text() == self.cPassword.text():
                password = self.password.text()
                print("Login Successful, email:" + email + ", password: " + password)
                hand = HandWindow()
                widget.addWidget(hand)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                msg = QMessageBox(text="Incorrect password!", parent=self)
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
        except:
                err = QMessageBox(text="A fatal error occured, please retry...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()
        
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
        self.home.clicked.connect(self.goToMenu)
        self.setWindowTitle("Register")

    def goToLog(self):
        login = LoginWindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def reigsterUser(self):
        try:
            name = self.name.text()
            surname = self.surname.text()
            email = self.email.text()
            if self.password.text() == self.cPassword.text():
                password = self.password.text()
                print("Registered Successfully! Welcome, " + name + " " + surname)
            else:
                msg = QMessageBox(text="Passwords do not match!", parent=self)
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
        except:
                err = QMessageBox(text="A fatal error occured, please retry...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()
        

class PaperWindow(QDialog):
    def __init__(self):
        super(PaperWindow, self).__init__()
        uic.loadUi("paper.ui",self)
        self.calculate.clicked.connect(self.calculatePaper)
        self.hand.clicked.connect(self.goToHand)
        self.home.clicked.connect(self.goToMenu)
        self.salarySlider.valueChanged.connect(self.display)
        self.setWindowTitle("Calculate: On Paper")

    def goToHand(self):
        hand = HandWindow()
        widget.addWidget(hand)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def calculatePaper(self):
        try:
            name = self.name.text()
        except:
                err = QMessageBox(text="A fatal error occured, please retry...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()
        
    def display(self):
        salary = self.salary.text()
        self.salary.setText(str(self.sender().value()))

class HandWindow(QDialog):
    def __init__(self):
        super(HandWindow, self).__init__()
        uic.loadUi("hand.ui",self)
        self.calculate.clicked.connect(self.calculateHand)
        self.paper.clicked.connect(self.goToPaper)
        self.home.clicked.connect(self.goToMenu)
        self.salarySlider.valueChanged.connect(self.display)
        self.setWindowTitle("Calculate: On Hand")


    def goToPaper(self):
        paper = PaperWindow()
        widget.addWidget(paper)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def calculateHand(self):
        try:
            salary = int(self.salary.text())
            taxDeduc = salary / 9.52
            dep = int(self.depBox.currentText())


            if(str(self.taxBox.currentText())) == "No":
                taxRelief = int(self.taxRelief.text()) * 0.2
                civilTax = salary / 4.785 - taxRelief

                onHand = salary - taxDeduc - civilTax - taxRelief
                self.Salary.setText(str(round(onHand, 2)))
            else:
                onHand = salary - taxDeduc + 250 * dep
                self.Salary.setText(str(round(onHand, 2)))
        except:
                err = QMessageBox(text="A fatal error occured, please retry...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()

    def display(self):
        salary = self.salary.text()
        self.salary.setText(str(self.sender().value()))


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