"""
for x in range(8,10):
    print(x)

for x in range(1,12,3):
    print(x)
"""
soma = 0
for i in range(1, 4):
    nota = float(input(f"informe a sua nota {i}: "))

    soma = soma + nota
print("A média é: ",soma /3)
