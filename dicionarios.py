#Dicionários
#criando dicionários
dicionario = {}
dicionario = dict()
dicionario = {'nome': 'mari', 'idade': 27, 'altura': 1.50}
print(dicionario)
print(dicionario['idade'])

#Adicionando elementos em um dicionário
dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 1.60
print(dicionario)

#Iterando sobre um dicionario
for chave in dicionario:#percore as chaves
    print(chave, dicionario[chave])

#Testando a existência de uma chave
print('peso' in dicionario)
print('altura' in dicionario)