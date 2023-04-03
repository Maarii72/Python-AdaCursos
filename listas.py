# Listas
#antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#com lista
notas = [7.9, 9.7, 8.2]

#criando listas
lista = []
lista = list()
lista = [27, "oi", False, 3.665]
lista_de_listas = [10, [1, 2]]

#Indexação e Slices(fatiamento)
lista = [27, "oi", False, 3.665]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])

print(lista[-1])#ultimo elemento
print(lista[-2])#penultimo elemento

#slices
lista = [10,20,50,70,85,94,65]
print(lista[0:3])# começa do indice 0 e vai ate o menor que 3, no caso até 2
print(lista[2:])# vai ate o final
print(lista[2:6:2])# pular em dois em dois

#Iteraçõrs com For
# utilizando os proprios elementos da lista
for elemento in lista: print(elemento)

#utilizando os índices
print('Comprimento da lista: ',len(lista))

for i in range(len(lista)): print(lista[i])