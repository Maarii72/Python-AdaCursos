#12. Exercício II
"""
Questão 1
Em Python é possível utilizar expressões condicionais para o direcionamento de 
fluxo do código. Considere o trecho de código a seguir:
O código acima informa se o número inteiro informado pelo usuário (e armazenado 
na variável x) é positivo ou negativo e par ou ímpar. Por exemplo, caso o 
usuário digite o número -42, o output esperado é:

O número -42 é negativo e par.

Para que este output seja possível, pelo que devemos substituir XXX e *** no 
código acima, respectivamente?
resposta: x < 0 e x % 2 == 0
"""
x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"
    

print(f"O número {x} é {resp1} e {resp2}.".format(x, resp1, resp2))

########################################################################
#Questão 2
"""
É muito frequente o uso de programação para a automação de tarefas repetitivas, 
sendo possível devido às estruturas de repetição. Em python, uma dessas 
estruturas é o laço while, que determina que um bloco de código seja repetido 
enquanto uma dada condição for verdadeira. Observe o código a seguir:
Ao ser executado, o que o trecho de código acima mostra na tela?
resposta: A soma dos n (no caso, n = 1000) primeiros termos da série 1, 1/2, 1/4, 1/8,...


cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)
"""


###############################################################################
#Questão 3
"""
Além do laço de repetição while, muitas vezes utilizamos o operador for em 
Python para implementarmos laços de repetição. Embora isso seja possível, o for 
é mais do que meramente um laço de repetição: este operador é utilizado para 
percorrer alguma estrutura iterável.
Quando queremos utilizar o for explicitamente como um laço de repetição, é muito 
comum utilizarmos a estrutura acima, com o auxílio do iterador range(). No 
entanto, o mesmo comportamento é possível se nos aproveitarmos do fato de que o 
for percorre qualquer iterável. Sabendo disso, das alternativas a seguir, qual 
é a única que NÃO reproduz o mesmo resultado que o trecho acima?

resposta: for _ in [10]:
    print("Olá, mundo!")
"""
for _ in range(10):
  print("Olá, mundo!") 

###############################################################################
#Questão 4
"""
Utilizamos listas para armazenar em um único objeto uma coleção de valores. 
Muitas vezes, desejamos criar uma nova lista a partir de uma lista original. 
Observe o código abaixo:
Qual deve ser o valor de A, B, C e D, respectivamente, para que o código acima 
gere a seguinte lista_final: [10, 10, 14, 6, 42, 126, 8, 10, 26]?
resposta:-item, item, -2*item, 2*item
"""
lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item)
    
        else:

            lista_final.append(item)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
    
        else:

            lista_final.append(2*item)
print(lista_final)

#############################################################################
#Questão 5
"""
Algumas funções podem nos ajudar a trabalhar com listas. Observe o código abaixo 
e o respectivo output desejado:
Output desejado:

> ['coelho', 'macaco', 'girafa']
> 3
> 0
Respectivamente, por quais funções devemos substituir função1, função2 e função3 
no código acima, para obter o output desejado?
resposta: remove, len, index
"""
animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))
