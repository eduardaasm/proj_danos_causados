import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from danos import Ui_MainWindow

class Principal(Ui_MainWindow , QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page_login)
        self.frame_msg_erro.hide()
        self.set_label_img(self.label_logo, 'imagem/engenharia_logo.png')
        self.set_label_img(self.label_icone, 'imagem/engenharia_logo.png')
        self.frame_msg_bar.hide()

        self.pushButton_entrar.clicked.connect(self.realizar_login)
        self.pushButton_cadastrar.clicked.connect(self.vai_cadastrar_endereco)

    def vai_cadastrar_endereco(self):
        self.stackedWidget.setCurrentWidget(self.page_cadastro)


    def realizar_login(self):
        print(self.lineEdit_login.text())
        usuario = self.lineEdit_login.text()
        print(self.lineEdit_senha.text())
        senha = self.lineEdit_senha.text()

        if usuario == 'fecadm' and senha == '1234':
            print('sucesso')
            self.stackedWidget.setCurrentWidget(self.page_cadastrar)
        else:
            self.frame_msg_erro.show()
        
         
    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)
        
if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    p = Principal()
    p.show()
    aplicacao.exec()


