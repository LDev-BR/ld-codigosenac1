def alunos():
    alunos = []
    while True:
        aluno = input("Nome do aluno: ")
        if aluno.lower() == "sair":
            break
        else:
            alunos.append(aluno)
    print(alunos)
alunos()