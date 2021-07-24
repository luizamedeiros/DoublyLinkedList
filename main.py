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

print("----Mostrando a lista deposis de inserir o elemento Barbara -----")
listaEncadeada.printa_lista()

# Inserindo um elemento antes do atual 
listaEncadeada.inserir_antes_do_atual("Lucas")

print("----Mostrando a lista depois de inserir o elemento Lucas -----")
listaEncadeada.printa_lista()

# Inserindo um elemento depois do atual 
listaEncadeada.inserir_depois_do_atual("Fernanda")

print("---- Mostrando o atual  -----")
listaEncadeada.acessar_atual()

# Excluindo o atual
listaEncadeada.excluir_atual()

print(" \n----Mostrando a lista depois de excluir o atual -----")
listaEncadeada.printa_lista()

# Excluir elemento
listaEncadeada.excluir_elemento("Eduarda")

print(" \n----Mostrando a lista depois de excluir o  elemento Eduarda -----")
listaEncadeada.printa_lista()

# Excluir ultimo elemento
listaEncadeada.excluir_ultimo()

print(" \n----Mostrando a lista depois de excluir o ultimo elemento -----")
listaEncadeada.printa_lista()

# Encontrar posição
posicao = listaEncadeada.posicao_de_k("Lucas")
print(" \n----Mostrando a posição do elemento Lucas -----")
print(f'A posição de Lucas é {posicao}')

# Verificando se a lista está vazia 
print(" \n----Mostrando a lista está vazia -----")
listaEncadeada.vazia()


