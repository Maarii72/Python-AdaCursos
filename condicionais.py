idade = 10
if idade >= 18:
    print("você é maior de idade.")
else:
    print("Você é menor de idade.")

"""
  Aprovado(a) se  media >= 7
  Reprovado(a) se media < 7
"""

nota1 = float(
        input("Digite a nota1? ")
        )

nota2 = float(
        input("Digite a nota2? ")
        )

presenca = int(
        input("Digite a presença? ")
        )

media = (nota1 + nota2)/2
#print(media,type(media))

if media >= 7 and presenca >= 70 : print("Você foi APROVADO, média:", media, " Presença:", presenca,"%")
elif media >= 5 and presenca >= 70 : print("RECUPERAÇÃO, média:", media, " Presença:", presenca,"%")
else : print("Você foi REPROVADO, média:", media, " Presença:", presenca,"%")
