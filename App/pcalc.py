import sys, re, mysql.connector 
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QLineEdit
from reportlab.pdfgen.canvas import Canvas


FIXED_WIDTH = 860
FIXED_HEIGHT = 720

def passValidation(password):
        specialS = ['$', '#', '@', '%']
        # A good password must have more than 6 characters, but less than 20 + one number in it + one upper case character in it +
        # one lower case character in it and one symbol (@#$%).
        if len(password) < 6 or len(password) > 20:
            err = QMessageBox(text="A password should be between 6 and 20 characters in length.")
            err.setIcon(QMessageBox.Icon.Warning)
            err.setStandardButtons(QMessageBox.StandardButton.Ok)
            err.setDefaultButton(QMessageBox.StandardButton.Ok)
            err.exec()
            return False;
        if not any(char.isdigit() for char in password):
            err = QMessageBox(text="A password should have atleast one numerical symbol in it.")
            err.setIcon(QMessageBox.Icon.Warning)
            err.setStandardButtons(QMessageBox.StandardButton.Ok)
            err.setDefaultButton(QMessageBox.StandardButton.Ok)
            err.exec()
            return False;
        if not any(char.isupper() for char in password):
            err = QMessageBox(text="A password should have atleast one upper case letter in it.")
            err.setIcon(QMessageBox.Icon.Warning)
            err.setStandardButtons(QMessageBox.StandardButton.Ok)
            err.setDefaultButton(QMessageBox.StandardButton.Ok)
            err.exec()
            return False;
        if not any(char.islower() for char in password):
            err = QMessageBox(text="A password should have atleast one lower case letter in it.")
            err.setIcon(QMessageBox.Icon.Warning)
            err.setStandardButtons(QMessageBox.StandardButton.Ok)
            err.setDefaultButton(QMessageBox.StandardButton.Ok)
            err.exec()
            return False;
        if not any(char in specialS for char in password):
            err = QMessageBox(text="A password should have atleast one of these symbols: @#$%")
            err.setIcon(QMessageBox.Icon.Warning)
            err.setStandardButtons(QMessageBox.StandardButton.Ok)
            err.setDefaultButton(QMessageBox.StandardButton.Ok)
            err.exec()
            return False;
            
    
        else:
            return True;

def emailValidation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex,email):
        return True;
    else:
        err = QMessageBox(text="Your email is not valid, please enter a valid email adress.")
        err.setIcon(QMessageBox.Icon.Warning)
        err.setStandardButtons(QMessageBox.StandardButton.Ok)
        err.setDefaultButton(QMessageBox.StandardButton.Ok)
        err.exec()
        return False;

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
        self.passBox.toggled.connect(self.showPassword)
        self.setWindowTitle("Login")

    def showPassword(self):
        if self.password.echoMode() == QLineEdit.EchoMode.Normal:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
    def loginUser(self):
        try:
            email = self.email.text()
            password = self.password.text()
            database = mysql.connector.connect(host = "localhost", user = "username", password = "Password1", database = "algascalc")
            cursor = database.cursor()  

            cursor.execute("SELECT email, password from userdata")
            fetch = cursor.fetchall()
            cursor.close()
            database.close()
            for x in fetch:
                if x[0] == email:
                    if x[1] == password:
                        hand = HandWindow()
                        widget.addWidget(hand)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        break
                err = QMessageBox(text="Login failed, incorrect email or password...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()
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
        self.passBox.toggled.connect(self.showPassword)
        self.setWindowTitle("Register")

    def showPassword(self):
        if self.password.echoMode() == QLineEdit.EchoMode.Normal:
            if self.cPassword.echoMode() == QLineEdit.EchoMode.Normal:
                self.password.setEchoMode(QLineEdit.EchoMode.Password)
                self.cPassword.setEchoMode(QLineEdit.EchoMode.Password)
        elif self.password.echoMode() == QLineEdit.EchoMode.Password:
            if self.cPassword.EchoMode() == QLineEdit.EchoMode.Password:
                self.password.setEchoMode(QLineEdit.EchoMode.Normal)
                self.cPassword.setEchoMode(QLineEdit.EchoMode.Normal)

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
            if emailValidation(self.email.text()):
                email = self.email.text()
            if self.password.text() == self.cPassword.text():
                
                try:
                # Example register pass : Passwords1@
                    database = mysql.connector.connect(host = "localhost", user = "username", password = "Password1", database = "algascalc")
                    cursor = database.cursor()  
                    if passValidation(self.password.text()):
                        password = self.password.text()


                    insert = ("INSERT INTO userdata (name, surname, email, password) VALUES (%s, %s, %s, %s)")
                    data = (name, surname, email, password)
                    cursor.execute(insert, data)
                    database.commit()
                    cursor.close()
                    database.close()

                    menu = HomeWindow()
                    widget.addWidget(menu)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                except:
                    msg = QMessageBox(text="Registration unsuccesful, check if everything is input correctly...", parent=self)
                    msg.setIcon(QMessageBox.Icon.Information)
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg.exec()
                
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
    

class HandWindow(QDialog):
    def __init__(self):
        super(HandWindow, self).__init__()
        uic.loadUi("hand.ui",self)
        self.calculate.clicked.connect(self.calculateHand)
        self.home.clicked.connect(self.goToMenu)
        self.pdfBtn.clicked.connect(self.pdfCreate)
        self.salarySlider.valueChanged.connect(self.display)
        self.setWindowTitle("Calculate: On Hand")

    def goToMenu(self):
        menu = HomeWindow()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def calculateHand(self):
        try:
            salary = int(self.salary.text())
            dep = int(self.depBox.currentText())
            taxBook = self.taxBox.currentText()

            if str(taxBook) == "Yes":
                salary = salary - (salary * 0.105)
                salary = salary - (salary * 0.2)
                self.Salary.setText(str(round(salary, 2)))
            elif str(taxBook) == "No":
                vsaoi = salary * 0.105
                salary = salary - vsaoi - (salary * 0.23 - vsaoi * 0.2)
                return salary
                self.Salary.setText(str(round(salary, 2)))

        except:
                err = QMessageBox(text="A fatal error occured, please retry...", parent=self)
                err.setIcon(QMessageBox.Icon.Critical)
                err.setStandardButtons(QMessageBox.StandardButton.Ok)
                err.setDefaultButton(QMessageBox.StandardButton.Ok)
                err.exec()
    
    def display(self):
        salary = self.salary.text()
        self.salary.setText(str(self.sender().value()))

    def pdfCreate(self):
        canvas = Canvas("Paycheck.pdf")
        salary = self.Salary.text()
        taxBook = self.taxBox.currentText()
        dep = self.depBox.currentText()

        canvas.setFont("Times-Roman", 25)
        canvas.drawString(0, 0, salary)
        canvas.save()
        


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
homewindow = HomeWindow()
widget.addWidget(homewindow)

widget.setFixedSize(FIXED_WIDTH, FIXED_HEIGHT)
widget.show()

#print(database)

try:
    sys.exit(app.exec())
except:
    print("Exiting")