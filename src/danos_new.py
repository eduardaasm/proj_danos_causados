# Form implementation generated from reading ui file 'danos_new.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.frame_login = QtWidgets.QFrame(parent=self.page_login)
        self.frame_login.setGeometry(QtCore.QRect(70, 210, 681, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_login.sizePolicy().hasHeightForWidth())
        self.frame_login.setSizePolicy(sizePolicy)
        self.frame_login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login.setObjectName("frame_login")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_senha = QtWidgets.QLineEdit(parent=self.frame_login)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_senha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.gridLayout_2.addWidget(self.lineEdit_senha, 2, 1, 1, 1)
        self.lineEdit_login = QtWidgets.QLineEdit(parent=self.frame_login)
        self.lineEdit_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.gridLayout_2.addWidget(self.lineEdit_login, 1, 1, 1, 1)
        self.pushButton_entrar = QtWidgets.QPushButton(parent=self.frame_login)
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        self.gridLayout_2.addWidget(self.pushButton_entrar, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        self.label_icone = QtWidgets.QLabel(parent=self.page_login)
        self.label_icone.setGeometry(QtCore.QRect(340, 60, 141, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icone.sizePolicy().hasHeightForWidth())
        self.label_icone.setSizePolicy(sizePolicy)
        self.label_icone.setMinimumSize(QtCore.QSize(141, 141))
        self.label_icone.setMaximumSize(QtCore.QSize(141, 141))
        self.label_icone.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_icone.setObjectName("label_icone")
        self.frame_msg_erro = QtWidgets.QFrame(parent=self.page_login)
        self.frame_msg_erro.setGeometry(QtCore.QRect(70, 320, 681, 71))
        self.frame_msg_erro.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_erro.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_erro.setObjectName("frame_msg_erro")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_msg_erro)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_msg_erro = QtWidgets.QLabel(parent=self.frame_msg_erro)
        self.label_msg_erro.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_msg_erro.sizePolicy().hasHeightForWidth())
        self.label_msg_erro.setSizePolicy(sizePolicy)
        self.label_msg_erro.setMinimumSize(QtCore.QSize(0, 25))
        self.label_msg_erro.setStyleSheet("background-color: rgb(255, 96, 117);")
        self.label_msg_erro.setObjectName("label_msg_erro")
        self.horizontalLayout.addWidget(self.label_msg_erro)
        self.pushButton_fechar_msg_erro = QtWidgets.QPushButton(parent=self.frame_msg_erro)
        self.pushButton_fechar_msg_erro.setObjectName("pushButton_fechar_msg_erro")
        self.horizontalLayout.addWidget(self.pushButton_fechar_msg_erro)
        self.stackedWidget.addWidget(self.page_login)
        self.page_cadastro = QtWidgets.QWidget()
        self.page_cadastro.setObjectName("page_cadastro")
        self.frame_5 = QtWidgets.QFrame(parent=self.page_cadastro)
        self.frame_5.setGeometry(QtCore.QRect(20, 69, 811, 431))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_logo = QtWidgets.QLabel(parent=self.frame_5)
        self.label_logo.setGeometry(QtCore.QRect(24, 25, 121, 91))
        self.label_logo.setObjectName("label_logo")
        self.frame_msg_bar = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_msg_bar.setGeometry(QtCore.QRect(110, 30, 661, 80))
        self.frame_msg_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_bar.setObjectName("frame_msg_bar")
        self.label_msg_bar = QtWidgets.QLabel(parent=self.frame_msg_bar)
        self.label_msg_bar.setGeometry(QtCore.QRect(40, 15, 471, 31))
        self.label_msg_bar.setObjectName("label_msg_bar")
        self.pushButton_fechar_msg = QtWidgets.QPushButton(parent=self.frame_msg_bar)
        self.pushButton_fechar_msg.setGeometry(QtCore.QRect(510, 20, 101, 28))
        self.pushButton_fechar_msg.setObjectName("pushButton_fechar_msg")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.frame_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 116, 721, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 11, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_nao = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_nao.setObjectName("radioButton_nao")
        self.gridLayout.addWidget(self.radioButton_nao, 3, 2, 1, 1)
        self.label_endereco = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_endereco.setObjectName("label_endereco")
        self.gridLayout.addWidget(self.label_endereco, 1, 0, 1, 1)
        self.label_apresenta_dano = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_apresenta_dano.setObjectName("label_apresenta_dano")
        self.gridLayout.addWidget(self.label_apresenta_dano, 3, 0, 1, 1)
        self.radioButton_sim = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_sim.setObjectName("radioButton_sim")
        self.gridLayout.addWidget(self.radioButton_sim, 3, 1, 1, 1)
        self.pushButton_pagina_anterior = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_pagina_anterior.setObjectName("pushButton_pagina_anterior")
        self.gridLayout.addWidget(self.pushButton_pagina_anterior, 6, 0, 1, 3)
        self.label_nome = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.gridLayout.addWidget(self.pushButton_salvar, 5, 0, 1, 3)
        self.lineEdit_quais_danos = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_quais_danos.setObjectName("lineEdit_quais_danos")
        self.gridLayout.addWidget(self.lineEdit_quais_danos, 4, 1, 1, 2)
        self.label_quais_danos = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_quais_danos.setObjectName("label_quais_danos")
        self.gridLayout.addWidget(self.label_quais_danos, 4, 0, 1, 1)
        self.label_maior_risco = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_maior_risco.setObjectName("label_maior_risco")
        self.gridLayout.addWidget(self.label_maior_risco, 2, 0, 1, 1)
        self.lineEdit_material = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_material.setText("")
        self.lineEdit_material.setObjectName("lineEdit_material")
        self.gridLayout.addWidget(self.lineEdit_material, 0, 1, 1, 2)
        self.lineEdit_quantidade = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        self.gridLayout.addWidget(self.lineEdit_quantidade, 1, 1, 1, 2)
        self.lineEdit_maior_risco = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_maior_risco.setObjectName("lineEdit_maior_risco")
        self.gridLayout.addWidget(self.lineEdit_maior_risco, 2, 1, 1, 2)
        self.stackedWidget.addWidget(self.page_cadastro)
        self.page_listar_dados = QtWidgets.QWidget()
        self.page_listar_dados.setObjectName("page_listar_dados")
        self.frame_listagem = QtWidgets.QFrame(parent=self.page_listar_dados)
        self.frame_listagem.setGeometry(QtCore.QRect(20, 29, 781, 521))
        self.frame_listagem.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_listagem.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_listagem.setObjectName("frame_listagem")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_listagem)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 601, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.frame_botoes_salvar_alterar = QtWidgets.QFrame(parent=self.frame_listagem)
        self.frame_botoes_salvar_alterar.setGeometry(QtCore.QRect(640, 40, 117, 281))
        self.frame_botoes_salvar_alterar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_botoes_salvar_alterar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_botoes_salvar_alterar.setObjectName("frame_botoes_salvar_alterar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_botoes_salvar_alterar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_salvar_processo = QtWidgets.QPushButton(parent=self.frame_botoes_salvar_alterar)
        self.pushButton_salvar_processo.setObjectName("pushButton_salvar_processo")
        self.verticalLayout.addWidget(self.pushButton_salvar_processo)
        self.pushButton_alterar = QtWidgets.QPushButton(parent=self.frame_botoes_salvar_alterar)
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.verticalLayout.addWidget(self.pushButton_alterar)
        self.pushButton_voltar_pag = QtWidgets.QPushButton(parent=self.frame_botoes_salvar_alterar)
        self.pushButton_voltar_pag.setObjectName("pushButton_voltar_pag")
        self.verticalLayout.addWidget(self.pushButton_voltar_pag)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page_listar_dados)
        self.page_cadastrar = QtWidgets.QWidget()
        self.page_cadastrar.setObjectName("page_cadastrar")
        self.frame_cadastro = QtWidgets.QFrame(parent=self.page_cadastrar)
        self.frame_cadastro.setGeometry(QtCore.QRect(29, 29, 771, 461))
        self.frame_cadastro.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastro.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastro.setObjectName("frame_cadastro")
        self.label_logo_page_cadastrar = QtWidgets.QLabel(parent=self.frame_cadastro)
        self.label_logo_page_cadastrar.setGeometry(QtCore.QRect(40, 20, 161, 151))
        self.label_logo_page_cadastrar.setObjectName("label_logo_page_cadastrar")
        self.pushButton_cadastrar = QtWidgets.QPushButton(parent=self.frame_cadastro)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(400, 60, 93, 28))
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.pushButton_listar = QtWidgets.QPushButton(parent=self.frame_cadastro)
        self.pushButton_listar.setGeometry(QtCore.QRect(400, 150, 93, 28))
        self.pushButton_listar.setObjectName("pushButton_listar")
        self.pushButton_sair_sistema = QtWidgets.QPushButton(parent=self.frame_cadastro)
        self.pushButton_sair_sistema.setGeometry(QtCore.QRect(400, 270, 101, 28))
        self.pushButton_sair_sistema.setObjectName("pushButton_sair_sistema")
        self.stackedWidget.addWidget(self.page_cadastrar)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_fechar_msg.clicked.connect(self.frame_msg_bar.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.lineEdit_login.setPlaceholderText(_translate("MainWindow", "Login"))
        self.pushButton_entrar.setText(_translate("MainWindow", "Entrar"))
        self.label_icone.setText(_translate("MainWindow", "Ícone"))
        self.label_msg_erro.setText(_translate("MainWindow", "Usuário ou senha incorretos"))
        self.pushButton_fechar_msg_erro.setText(_translate("MainWindow", "X"))
        self.label_logo.setText(_translate("MainWindow", "Logo"))
        self.label_msg_bar.setText(_translate("MainWindow", "Erro de Cadastro"))
        self.pushButton_fechar_msg.setText(_translate("MainWindow", "X"))
        self.radioButton_nao.setText(_translate("MainWindow", "Não"))
        self.label_endereco.setText(_translate("MainWindow", "Endereço:"))
        self.label_apresenta_dano.setText(_translate("MainWindow", "Apresenta algum dano causado pela proximidade ao rio ?"))
        self.radioButton_sim.setText(_translate("MainWindow", "Sim"))
        self.pushButton_pagina_anterior.setText(_translate("MainWindow", "Voltar"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        self.label_quais_danos.setText(_translate("MainWindow", "Quais os danos?"))
        self.label_maior_risco.setText(_translate("MainWindow", "Qual o maior risco de morar nas proximidades?"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Qual o maior risco de morar nas proximidades?"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apresenta algum dano causado pela proximidade ao rio ?"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quais os danos?"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_salvar_processo.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_alterar.setText(_translate("MainWindow", "Alterar"))
        self.pushButton_voltar_pag.setText(_translate("MainWindow", "Sair"))
        self.label_logo_page_cadastrar.setText(_translate("MainWindow", "Logo"))
        self.pushButton_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButton_listar.setText(_translate("MainWindow", "Listar"))
        self.pushButton_sair_sistema.setText(_translate("MainWindow", "Sair do Sistema"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
