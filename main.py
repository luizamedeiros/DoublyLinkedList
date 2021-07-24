from item import Item


class ListaEncadeada:
    def __init__(self):
        self.__head = None
        self.__cursor = None

    def inserir_na_frente(self, item):
        if self.__head is not None:
            self.__cursor = self.__head
            novo_item = Item(item)
            novo_item.prox = self.__cursor
            self.__head = novo_item
        else:
            novo_item = Item(item)
            novo_item.prox = None
            self.__head = novo_item

    def inserir_no_fim(self, item):
        if self.__head is not None:
            self.__cursor = self.__head
            novo_item = Item(item)
            while self.__cursor.prox:
                self.__cursor = self.__cursor.prox
            self.__cursor.prox = novo_item
            novo_item.prox = None
            novo_item.ante = self.__cursor
            self.__cursor = novo_item
        else:
            novo_item = Item(item)
            novo_item.prox = None
            self.__head = novo_item

    def printa_lista(self):
        cur = self.__head
        while cur:
            print(cur.item)
            cur = cur.prox

    def buscar(self, item):
        encontrado = False
        self.__cursor = self.__head
        while self.__cursor.prox:
            self.__cursor = self.__cursor.prox
            if str(self.__cursor.item) == str(item):
                encontrado = True
                return encontrado
        return encontrado

    def excluir_primeiro(self):
        self.__head = self.__head.prox

    def excluir_ultimo(self):
        self.__ir_para_ultimo()
        penultimo = self.__cursor.ante
        penultimo.prox = None
        print("Excluí o último lugar")

    def inserir_na_posicao(self, k, item):
        k -= 1
        novo_item = Item(item)
        self.__ir_para_primeira()
        self.__avancar_k_posicoes(k)
        self.inserir_antes_do_atual(novo_item.item)

#rever else
    def acessar_atual(self):
        if (self.__head is not None) and self.__head.prox:
            print("Eu sou o atual: " + str(self.__cursor.item))
            return self.__cursor.item
        elif self.__head is not None and (not self.__head.prox):
            print("Eu sou o atual: " + str(self.__head.item))
        else:
            return None


    def inserir_antes_do_atual(self, item):
        item_pre_alteracao = self.__cursor.ante
        item_pos_alteracao = self.__cursor
        novo_item = Item(item)
        item_pre_alteracao.prox = novo_item
        item_pos_alteracao.ante = novo_item
        novo_item.ante = item_pre_alteracao
        novo_item.prox = item_pos_alteracao

    def inserir_depois_do_atual(self, item):
        item_pre_alteracao = self.__cursor
        item_pos_alteracao = self.__cursor.prox
        novo_item = Item(item)
        item_pre_alteracao.prox = novo_item
        item_pos_alteracao.ante = novo_item
        novo_item.ante = item_pre_alteracao
        novo_item.prox = item_pos_alteracao

    def excluir_atual(self):
        if not self.__head.prox:
            self.excluir_primeiro()
        elif self.__cursor.prox is None:
            self.excluir_ultimo()
        else:
            item_a_ligar = self.__cursor.prox
            item_a_excluir = self.__cursor
            item_anterior = self.__cursor.ante
            item_anterior.prox = item_a_excluir.prox
            item_a_ligar.antes = item_anterior

#FUNÇÕES PARA CONTROLE DE CURSOR
    def __ir_para_primeira(self):
        self.__cursor = self.__head

    def __ir_para_ultimo(self):
        while self.__cursor.prox is not None:
            self.__cursor = self.__cursor.prox

    def __retroceder_k_posicoes(self, k):
        contador = 0
        while contador <= k:
            self.__cursor = self.__cursor.ante
            contador += 1

    def __avancar_k_posicoes(self, k):
        contador = 0
        while contador <= k:
            if self.__cursor.prox is not None:
                self.__cursor = self.__cursor.prox
                contador += 1
            else:
                print("Lista extrapolada!")
                return "Lista extrapolada!"


#OUTROS
    def vazia(self):
        if self.__head is None:
            print(True)
            return True
        else:
            print(False)
            return False

    def posicao_de_k(self, item):
        self.__ir_para_primeira()
        contador = 0
        while str(self.__cursor.item) != str(item) and self.__cursor.prox:
            self.__cursor = self.__cursor.prox
            contador += 1
        if str(self.__cursor.item) == str(item):
            print(f'Posição de {item} é {contador}')
            return int(contador)
        elif self.__cursor.prox is None:
            print("O item solicitado é inexistente \n")
            return False
        else:
            print(int(contador))
            return int(contador)

    def excluir_elemento(self, item):
        pos = self.posicao_de_k(item)
        if not pos:
            pass
        else:
            self.excluir_atual()

