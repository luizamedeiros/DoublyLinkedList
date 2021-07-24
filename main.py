from doublyLinkedList import ListaEncadeada

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
 
# Buscando um elemento que existe na lista - true
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
listaEncadeada.excluir_ultimo()
 
print("----Mostrando a lista depois de excluir o ultimo elemento-----")
listaEncadeada.printa_lista()

# Inserindo um elemento em determinada posição
listaEncadeada.inserir_na_posicao(2, "Barbara")

print("----Mostrando a lista depois de adicionar o item Barbara na segunda posição -----")
listaEncadeada.printa_lista()

listaEncadeada.acessar_atual()
