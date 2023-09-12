class Danos_new:
    def __init__(self, nome = None, endereco = None, maior_risco = None, apresenta_algum_dano = None, quais_danos = None ):
        self.error = ''
        self.nome = nome
        self.endereco = endereco
        self.maior_risco = maior_risco
        self.apresenta_algum_dano = apresenta_algum_dano
        self.quais_danos = quais_danos
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome != None and len(str(nome)) != 0:
            self.__nome = nome
        else:
            self.error = '"Nome" é obrigatório!'

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        if endereco != None and len(str(endereco)) != 0:
            self.__endereco = endereco
        else:
            self.error = '"Endereço" é um campo obrigatório'

    @property
    def maior_risco(self):
        return self.__maior_risco
    
    @maior_risco.setter
    def maior_risco(self, maior_risco):
        if maior_risco != None and len(maior_risco) != 0:
            self.__maior_risco = maior_risco
        else:
            self.error = '"Qual o  maior risco de morar nas proximidades?" é obrigatório'

    @property
    def apresenta_algum_dano(self):
        return self.__apresenta_algum_dano
    
    @apresenta_algum_dano.setter
    def apresenta_algum_dano(self, apresenta_algum_dano):
        if apresenta_algum_dano == None or apresenta_algum_dano == '':
            self.error = 'O "campo Apresenta algum dano causado pela proximidade ao rio?" é obrigatório'
        else:
            self.__apresenta_algum_dano = apresenta_algum_dano

    @property
    def quais_danos(self):
        return self.__quais_danos
    
    @quais_danos.setter
    def quais_danos(self, quais_danos):
        if quais_danos != None and len(str(quais_danos)) != 0:
            self.__quais_danos = quais_danos
        else:
            self.error = '"Quais danos?" é obrigatório'

    def __str__(self) -> str:
        apresenta_algum_dano = 'sim' if self.apresenta_algum_dano else 'não'
        return f'Nome: {self.nome} |\
                Endereco: {self.endereco} |\
                Maior_Risco: {self.maior_risco} |\
                Apresenta algum dano? {apresenta_algum_dano}|\
                Quais danos: {self.quais_danos}'

