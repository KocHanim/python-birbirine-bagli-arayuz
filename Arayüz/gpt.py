from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import login  # login ekranının olduğu dosyanın adı
import veri  # ikinci ekranın olduğu dosyanın adı


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        kadi = self.ui.lineEdit_kullanici_adi.text()
        sifre = self.ui.lineEdit_sifre.text()
        if kadi == "Rumeysa" and sifre == "123":
            self.second_window = SecondWindow()
            self.second_window.show()
            self.hide()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = veri.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())