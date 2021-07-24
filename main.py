from doublyLinkedList import ListaEncadeada

#Instanciando a lista
listaEncadeada = ListaEncadeada()

# Inserindo elementos na frente
listaEncadeada.inserir_na_frente("Luiza")
listaEncadeada.inserir_na_frente("Eduarda")
listaEncadeada.inserir_na_frente("Maria")
listaEncadeada.inserir_na_frente("Ana")

# Acessando elemento atual
listaEncadeada.acessar_atual()

# Inserindo elementos no fim
listaEncadeada.inserir_no_fim("Pedro")
listaEncadeada.inserir_no_fim("José")
listaEncadeada.inserir_no_fim("Marcus")

# Acessando elemento atual
listaEncadeada.acessar_atual()

# Buscando elemento que existe na lista - true
listaEncadeada.buscar("Eduarda")

# Buscando elemento que não existe na lista - false
listaEncadeada.buscar("Bruna")

print("----Mostrando a lista antes de excluir primeiro elemento-----")
listaEncadeada.printa_lista()

# Excluindo o primeiro elemento (Ana)
listaEncadeada.excluir_primeiro()

print("----Mostrando a lista depois de excluir primeiro elemento-----")
listaEncadeada.printa_lista()

# Excluindo o ultimo elemento (Marcus)
print("ir p ult")
listaEncadeada.ir_para_ultimo()

print("----Mostrando a lista depois de excluir o ultimo elemento-----")
listaEncadeada.printa_lista()
