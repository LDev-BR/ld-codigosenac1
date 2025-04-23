import math
def operacoes_matematicas():
    numero = float(input('Digite um número: '))
    raiz = math.sqrt(numero)
    seno = math.sin(numero)
    cosseno = math.cos(numero)
    logaritmo = math.log(numero)
    print('A raiz quadrada do número é: ', raiz)
    print('O seno do número é: ', seno)
    print('O cosseno do número é: ', cosseno)
    print('O logaritmo do número é: ', logaritmo)
operacoes_matematicas()