import random

numero_sorteado = random.randint(1,5)
numero_escolhido = int(input("Informe um número entre 1 e 5: "))

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente...")
    numero_escolhido = int(input("Informe um número entre 1 e 5: "))
print("Parabéns você acertou!")

#Estrutura com contador
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1