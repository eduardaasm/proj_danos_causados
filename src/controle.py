class Controle:

    def __init__(self) -> None:
        self.lista = None
        
    def inserir_final_lista(self,nodo):

        self.lista.append(nodo)
        return "Dados salvos com sucesso!"
    
    def inserir_posicao_lista(self,posicao,nodo):
        self.lista.insert(int(posicao), nodo)
        return f"item adicionado a posição{posicao}"
    
    def remover_da_lista(self,posicao = None):
        removeu = False
        if posicao == None:
            del self.lista[len(self.lista)-1]
            removeu = True
        else:
            posicao = int(posicao)
            if posicao < len(self.lista):
                del self.lista[int(posicao)]
                removeu = True
            else:
                return 'A posição especificada não existe', removeu
            return 'item removido com sucesso', removeu
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self):
        self.__lista = []
    
