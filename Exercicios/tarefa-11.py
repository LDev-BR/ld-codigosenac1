def fraude():
    ana = 0
    bruno = 0
    carla = 0
    print('''
    Qual operação você deseja executar?:
    (A) - Ana
    (B) - Bruno
    (C) - Carla
    ''')
    for i in range (5):
        voto = str(input('Digite o número: '))
        if voto == 'a':
            ana +=1
        elif voto == 'b':
            bruno +=1
        elif voto == 'c':
            carla +=1
        else:
            print('Erro')
    print(f'Ana: {ana}')
    print(f'Bruno: {bruno}')
    print(f'Carla: {carla}')

fraude()