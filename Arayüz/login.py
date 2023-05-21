from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 432)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 120, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 180, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_kullanici_adi = QtWidgets.QLineEdit(Form)
        self.lineEdit_kullanici_adi.setGeometry(QtCore.QRect(230, 120, 113, 22))
        self.lineEdit_kullanici_adi.setObjectName("lineEdit_kullanici_adi")
        self.lineEdit_sifre = QtWidgets.QLineEdit(Form)
        self.lineEdit_sifre.setGeometry(QtCore.QRect(230, 180, 113, 22))
        self.lineEdit_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre.setObjectName("lineEdit_sifre")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Kullanıcı Adı"))
        self.label_2.setText(_translate("Form", "Şifre"))
        self.pushButton.setText(_translate("Form", "Giriş Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
