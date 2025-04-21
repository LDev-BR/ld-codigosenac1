def colegio():
    total = []

    materia = input('Digite o nome da matéria: ')

    quantidade = int(input('Digite a quantidade de alunos: '))
    total_alunos = 1
    while total_alunos <= quantidade:
        nome = input('Digite o nome do aluno: ')
        nota = int(input('Digite a nota do aluno: '))
        print('Aluno cadastrado')
        total_alunos = total_alunos + 1
        classe = (nome, nota)
        total.append(classe)
    else:
        print('''
Todos os alunos foram cadastrados''')
    print('''
Quantidade de alunos cadastrados: ''', len(total))

    for n in total:
        nome = n[0]
        nota = n[1]
        print(f'({materia})', 'Aluno:', nome, '  Nota:', nota)
    dnvo()
def dnvo():
    novamente = input('''
Deseja cadastrar outra matéria?
S para SIM e N para NÂO.
''')
    if novamente.upper() == 'S':
        colegio()
    elif novamente.upper() == 'N':
        print('Obrigado por usar esta ferramente')
    else:
        print('Valor inválido, tente novamente')
        dnvo()
colegio()
