class Danos_control:

    def __init__(self) -> None:
        self.lista_dados = None

    def salvar_dados (self, danos):
        self.lista_dados.append(danos)

        return 'Dados salvos com sucesso'
