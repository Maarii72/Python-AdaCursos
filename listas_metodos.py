#Métodos de listas
lista = [1, 3, 12, 8, 2]

#append - adicionar elemento no final da lista
print("antes do append",lista)
lista.append(3)
print("depois do append",lista)

#insert - adicionar elemento escolhendo a posição
lista.insert(2, 10)# na posição 2 por o elemento 10
print("depois do insert: ",lista)

#extend - juntar duas listas
lista2 =[1,2,3]
lista.extend(lista2) #insere no final os elementos da lista2
print("depois do extend: ",lista)

#pop - remover o ultimo elemento
lista.pop()
print("Lista após o pop: ",lista)

lista.pop(0) #remove indicando o indice
print("Lista após o pop: ",lista)

#remove - qual elemento deseja remover(não o indice)
lista.remove(3) #remove o primeiro 3 encontrado
print("Lista após o remove: ",lista)

#count - conta quantas vezes o elemnto aparece na lista
print("Quantidade de 2 na lista: ",lista.count(2))

#index - indica o indice do elemento
print("Índice do elemento 12: ",lista.index(12))

#sort -ordenar
lista.sort() #ordem de forma crescente
print(lista)

lista.sort(reverse=True) #ordem de forma decrescente
print(lista)

#Funções para listas
#len - quantos elementos tenho na lista
print(len(lista))

#sum - soma elementos da lista
print(sum(lista))

#max - o maior valor da lista
print("Maior elemento da lista: ", max(lista))

#min - o menor valor da lista
print("Menor elemento da lista: ", min(lista))