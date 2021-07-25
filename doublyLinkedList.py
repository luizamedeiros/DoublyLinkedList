from item import Item


class ListaEncadeada:
    def __init__(self):
        self.__head = None
        self.__cursor = None
    
    # Método com finalidade de inserir o elemento no início da lista.
    def inserir_na_frente(self, item):
        if self.__head is not None:
            self.__cursor = self.__head
            novo_item = Item(item)
            novo_item.prox = self.__cursor
            self.__cursor.ante = novo_item
            self.__head = novo_item
            self._cursor = self.__head
        else:
            novo_item = Item(item)
            novo_item.prox = None
            self.__head = novo_item

    # Método com finalidade de inserir o elemento no final da lista. 
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

    # Método com finalidade de mostrar a lista
    def printa_lista(self):
        printer = self.__head
        while printer.prox:
            print(printer.item)
            printer = printer.prox

    # Método com finalidade de buscar um dado  elemento na lista
    def buscar(self, item):
        encontrado = False
        self.__cursor = self.__head
        while self.__cursor.prox:
            self.__cursor = self.__cursor.prox
            if str(self.__cursor.item) == str(item):
                encontrado = True
                print(f'O item {item} foi encontrado!')
                return encontrado
        print(f'O item {item} não foi encontrado!')
        return encontrado

    # Método com finalidade de excluir o primeiro elemento da lista
    def excluir_primeiro(self):
        self.__head = self.__head.prox

    # Método com finalidade de excluir o último  elemento da lista
    def excluir_ultimo(self):
        self.__ir_para_ultimo()
        self.__cursor.prox = None

    #  Método com finalidade de inserir um elemento em uma determinada posição (k) da lista
    def inserir_na_posicao(self, k, item):
        k -= 1
        novo_item = Item(item)
        self.__ir_para_primeira()
        self.__avancar_k_posicoes(k)
        self.inserir_antes_do_atual(novo_item.item)

    # Método com finalidade de indicar qual é o elemento atual (ponteiro / cursor)
    def acessar_atual(self):
        if (self.__head is not None) and self.__head.prox:
            print("Eu sou o atual: " + str(self.__cursor.item))
            return self.__cursor.item
        elif self.__head is not None and (not self.__head.prox):
            print("Eu sou o atual: " + str(self.__head.item))
        else:
            return None

    # Método com finalidade de inserir um elemento antes do elemento atual selecionado
    def inserir_antes_do_atual(self, item):
        item_pre_alteracao = self.__cursor.ante
        item_pos_alteracao = self.__cursor
        novo_item = Item(item)
        item_pre_alteracao.prox = novo_item
        item_pos_alteracao.ante = novo_item
        novo_item.ante = item_pre_alteracao
        novo_item.prox = item_pos_alteracao

    # Método com finalidade de inserir um elemento depois do elemento atual selecionado
    def inserir_depois_do_atual(self, item):
        item_pre_alteracao = self.__cursor
        item_pos_alteracao = self.__cursor.prox
        novo_item = Item(item)
        item_pre_alteracao.prox = novo_item
        item_pos_alteracao.ante = novo_item
        novo_item.ante = item_pre_alteracao
        novo_item.prox = item_pos_alteracao

    # Método com finalidade de excluir o  elemento atual selecionado
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
    
    #  Mover o ponteiro para a primeira posição
    def __ir_para_primeira(self):
        self.__cursor = self.__head

    # Mover o ponteiro para a última posição
    def __ir_para_ultimo(self):
        self.__ir_para_primeira()
        while self.__cursor.prox.prox:
            self.__cursor = self.__cursor.prox

    # Retrocede o ponteiro para a posição (k) desejada
    def __retroceder_k_posicoes(self, k):
        contador = 0
        while contador <= k:
            self.__cursor = self.__cursor.ante
            contador += 1
            
    # Avança o ponteiro para a posição (k) deseja
    def __avancar_k_posicoes(self, k):
        contador = 0
        while contador <= k:
            if self.__cursor.prox is not None:
                self.__cursor = self.__cursor.prox
                contador += 1
            else:
                print("Lista extrapolada!")
                return "Lista extrapolada!"

    # Método com finalidade de verificar se a lista está ou não vazia, retornando um valor booleano.
    def vazia(self):
        if self.__head is None:
            print(True)
            return True
        else:
            print(False)
            return False

    # Método com finalidade de verificar a posição de determinado elemento dentro da lista
    def posicao_de_k(self, item):
        self.__ir_para_primeira()
        contador = 0
        while str(self.__cursor.item) != str(item) and self.__cursor.prox:
            self.__cursor = self.__cursor.prox
            contador += 1
        if str(self.__cursor.item) == str(item):
            return int(contador)
        elif self.__cursor.prox is None:
            print("O item solicitado é inexistente \n")
            return False
        else:
            print(int(contador))
            return int(contador)

    # Método com finalidade de excluir um determinado elemento da lista
    def excluir_elemento(self, item):
        pos = self.posicao_de_k(item)
        if not pos:
            pass
        else:
            self.excluir_atual()

