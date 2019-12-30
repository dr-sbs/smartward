# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 690)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.signStack = QtWidgets.QStackedWidget(self.centralWidget)
        self.signStack.setGeometry(QtCore.QRect(0, 0, 601, 690))
        self.signStack.setMinimumSize(QtCore.QSize(0, 0))
        self.signStack.setMaximumSize(QtCore.QSize(1366, 768))
        self.signStack.setObjectName("signStack")
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setObjectName("signupPage")
        self.signupBox = QtWidgets.QGroupBox(self.signupPage)
        self.signupBox.setGeometry(QtCore.QRect(10, 10, 581, 671))
        self.signupBox.setStyleSheet(" background:transparent;\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"color: rgb(23, 109, 2);")
        self.signupBox.setTitle("")
        self.signupBox.setObjectName("signupBox")
        self.address = QtWidgets.QLineEdit(self.signupBox)
        self.address.setGeometry(QtCore.QRect(50, 290, 491, 31))
        self.address.setStyleSheet("background:transparent")
        self.address.setObjectName("address")
        self.signup = QtWidgets.QPushButton(self.signupBox)
        self.signup.setGeometry(QtCore.QRect(200, 580, 191, 41))
        self.signup.setStyleSheet("background:blue;\n"
"color:white;")
        self.signup.setObjectName("signup")
        self.municipality = QtWidgets.QLineEdit(self.signupBox)
        self.municipality.setGeometry(QtCore.QRect(50, 230, 351, 31))
        self.municipality.setStyleSheet("background:transparent")
        self.municipality.setText("")
        self.municipality.setObjectName("municipality")
        self.wardno = QtWidgets.QLineEdit(self.signupBox)
        self.wardno.setGeometry(QtCore.QRect(411, 230, 141, 31))
        self.wardno.setStyleSheet("background:transparent")
        self.wardno.setObjectName("wardno")
        self.phoneNo = QtWidgets.QLineEdit(self.signupBox)
        self.phoneNo.setGeometry(QtCore.QRect(50, 350, 351, 31))
        self.phoneNo.setStyleSheet("background:transparent")
        self.phoneNo.setText("")
        self.phoneNo.setObjectName("phoneNo")
        self.email = QtWidgets.QLineEdit(self.signupBox)
        self.email.setGeometry(QtCore.QRect(50, 410, 351, 31))
        self.email.setStyleSheet("background:transparent")
        self.email.setObjectName("email")
        self.mun_logo = QtWidgets.QLineEdit(self.signupBox)
        self.mun_logo.setGeometry(QtCore.QRect(50, 470, 351, 31))
        self.mun_logo.setStyleSheet("background:transparent")
        self.mun_logo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mun_logo.setObjectName("mun_logo")
        self.password = QtWidgets.QLineEdit(self.signupBox)
        self.password.setGeometry(QtCore.QRect(50, 520, 251, 31))
        self.password.setStyleSheet("background:transparent")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(self.signupBox)
        self.confirmpassword.setGeometry(QtCore.QRect(311, 520, 251, 31))
        self.confirmpassword.setStyleSheet("background:transparent")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.sw_logo_2 = QtWidgets.QLabel(self.signupBox)
        self.sw_logo_2.setGeometry(QtCore.QRect(140, 10, 311, 191))
        self.sw_logo_2.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/sw_logo.png)")
        self.sw_logo_2.setText("")
        self.sw_logo_2.setObjectName("sw_logo_2")
        self.signin_2 = QtWidgets.QPushButton(self.signupBox)
        self.signin_2.setGeometry(QtCore.QRect(288, 630, 261, 25))
        self.signin_2.setStyleSheet("border:none;")
        self.signin_2.setObjectName("signin_2")
        self.signStack.addWidget(self.signupPage)
        self.signinPage = QtWidgets.QWidget()
        self.signinPage.setObjectName("signinPage")
        self.signinBox = QtWidgets.QGroupBox(self.signinPage)
        self.signinBox.setGeometry(QtCore.QRect(10, 10, 581, 671))
        self.signinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.signinBox.setMaximumSize(QtCore.QSize(1366, 768))
        self.signinBox.setStyleSheet(" background:transparent;\n"
"color: rgb(23, 109, 2);\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;")
        self.signinBox.setTitle("")
        self.signinBox.setObjectName("signinBox")
        self.login_id = QtWidgets.QLineEdit(self.signinBox)
        self.login_id.setGeometry(QtCore.QRect(70, 270, 441, 41))
        self.login_id.setStyleSheet("background:transparent")
        self.login_id.setObjectName("login_id")
        self.login_password = QtWidgets.QLineEdit(self.signinBox)
        self.login_password.setGeometry(QtCore.QRect(70, 360, 441, 41))
        self.login_password.setStyleSheet("background:transparent;")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password.setObjectName("login_password")
        self.signin = QtWidgets.QPushButton(self.signinBox)
        self.signin.setGeometry(QtCore.QRect(180, 460, 211, 41))
        self.signin.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signin.setObjectName("signin")
        self.sw_logo = QtWidgets.QLabel(self.signinBox)
        self.sw_logo.setGeometry(QtCore.QRect(140, 10, 311, 191))
        self.sw_logo.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/sw_logo.png)")
        self.sw_logo.setText("")
        self.sw_logo.setObjectName("sw_logo")
        self.forgetPassword = QtWidgets.QPushButton(self.signinBox)
        self.forgetPassword.setGeometry(QtCore.QRect(318, 540, 151, 25))
        self.forgetPassword.setStyleSheet("border:none;")
        self.forgetPassword.setObjectName("forgetPassword")
        self.signup_2 = QtWidgets.QPushButton(self.signinBox)
        self.signup_2.setGeometry(QtCore.QRect(470, 540, 61, 25))
        self.signup_2.setStyleSheet("border:none;\n"
"border-left:50px;\n"
"")
        self.signup_2.setObjectName("signup_2")
        self.signStack.addWidget(self.signinPage)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.signStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartवडा"))
        self.address.setPlaceholderText(_translate("MainWindow", "Address"))
        self.signup.setText(_translate("MainWindow", "Sign Up"))
        self.municipality.setPlaceholderText(_translate("MainWindow", "Municipality/VDC"))
        self.wardno.setPlaceholderText(_translate("MainWindow", "Ward No."))
        self.phoneNo.setPlaceholderText(_translate("MainWindow", "Phone No,"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail ID"))
        self.mun_logo.setPlaceholderText(_translate("MainWindow", "Municipality/VDC Logo"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirmpassword.setPlaceholderText(_translate("MainWindow", "Re-Type your Password"))
        self.signin_2.setText(_translate("MainWindow", "Already have account,Sign In Instead"))
        self.login_id.setPlaceholderText(_translate("MainWindow", "Id or Gmail"))
        self.login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signin.setText(_translate("MainWindow", "Sign In"))
        self.forgetPassword.setText(_translate("MainWindow", "Forgot your password"))
        self.signup_2.setText(_translate("MainWindow", "|Sign Up"))
#import sw_rc