import sys
from model.novo import Danos_new
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from danos_new import Ui_MainWindow



class Principal(Ui_MainWindow , QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page_login)
        self.frame_msg_erro.hide()
        self.set_label_img(self.label_logo, 'imagem/engenharia_logo.png')
        self.set_label_img(self.label_icone, 'imagem/engenharia_logo.png')
        self.set_label_img(self.label_logo_page_cadastrar, 'imagem/engenharia_logo.png')
        self.frame_msg_bar.hide()
        self.lineEdit_login.setFocus()
        self.lista_de_danos = []

        self.pushButton_entrar.clicked.connect(self.realizar_login)
        self.pushButton_cadastrar.clicked.connect(self.vai_cadastrar_endereco)
        self.pushButton_listar.clicked.connect(self.listar_endereco)
        self.pushButton_sair_sistema.clicked.connect(self.voltar_acao)
        self.pushButton_voltar_pag.clicked.connect(self.voltar_pagina)
        self.pushButton_pagina_anterior.clicked.connect(self.voltar_pagina)
        self.pushButton_salvar.clicked.connect(self.salvar_dados)
        self.pushButton_fechar_msg_erro.clicked.connect(lambda : self.frame_msg_erro.hide())
        self.pushButton_voltar_pag.clicked.connect(self.pagina_inicial)


        

        
    def pagina_inicial(self):
        self.stackedWidget.setCurrentWidget(self.page_cadastrar)
       

    def salvar_dados(self):
        print(self.lineEdit_material.text())
        nome = self.lineEdit_material.text()
        print(self.lineEdit_quantidade.text())
        endereco = self.lineEdit_quantidade.text()
        print(self.lineEdit_maior_risco.text())
        maior_risco = self.lineEdit_maior_risco.text()
        print(self.lineEdit_quais_danos.text())
        apresenta_algum_dano = True if self.radioButton_sim.isChecked() else False       
        quais_danos = self.lineEdit_quais_danos.text()

        dano = Danos_new(nome, endereco, maior_risco,apresenta_algum_dano, quais_danos)

        if dano.error != '' :
            self.label_msg_bar.setText(dano.error)
            self.frame_msg_bar.show()
        else:
            self.lista_de_danos.append(dano)
            self.label_msg_bar.setText('Dados salvos com sucesso')
            self.frame_msg_bar.show()            

    def vai_cadastrar_endereco(self):
        self.stackedWidget.setCurrentWidget(self.page_cadastro)

    def listar_endereco(self):
        print(self.lista_de_danos)
        self.tableWidget.setRowCount(len(self.lista_de_danos))
        cont_linhas = 0
        for obj in self.lista_de_danos:
            print(obj.nome)
            self.tableWidget.setItem(cont_linhas, 0, QTableWidgetItem(obj.nome))
            self.tableWidget.setItem(cont_linhas, 1, QTableWidgetItem(str(obj.endereco)))
            self.tableWidget.setItem(cont_linhas, 2, QTableWidgetItem(str(obj.maior_risco)))
            self.tableWidget.setItem(cont_linhas, 3, QTableWidgetItem(str('Sim' if True else 'Não')))
            self.tableWidget.setItem(cont_linhas, 4, QTableWidgetItem(str(obj.quais_danos)))

            cont_linhas += 1

        self.stackedWidget.setCurrentWidget(self.page_listar_dados)

       
    



    def voltar_acao(self):
        self.stackedWidget.setCurrentWidget(self.page_login)

    def voltar_pagina(self):
        self.stackedWidget.setCurrentWidget(self.page_cadastrar)
        
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

