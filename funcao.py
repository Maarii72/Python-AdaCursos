#criação de funções
#função inicial
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')
saudacao()

#função de parâmetros
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')
saudacao('Mari', 'python')
saudacao('maria', 'java')

#função com parâmetros default
def saudacao(nome, curso='python'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')
saudacao('Mari')

#função com retorno
def soma(num1, num2):
    return num1 + num2
resultado = soma(5, 7)
print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
resultado = calculadora(10, 20, '/')
print(resultado)