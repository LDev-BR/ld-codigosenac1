def trabalho():
    valor = float(input('Valor da hora: '))
    horas = int(input('Horas trabalhadas: '))
    hora_extra = int(input('Valor da hora extra: '))
    if horas > 8:
        Total_dia = valor*horas*hora_extra
        print(f'Seu desconto é de: {Total_dia}')
    elif horas <= 8:
        Total_dia = valor*horas
        print(f'Seu desconto é de: {Total_dia}')
    else:
        print('Burro')

trabalho()