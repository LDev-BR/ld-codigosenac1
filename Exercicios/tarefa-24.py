def media_alunos():
    alunos = []
    for n in range(int(input("Quantidade de alunos: "))):
        nota = float(input(f"Nota do aluno: "))
        alunos.append(nota)
    print("As notas foram: ", alunos)
    media = sum(alunos) / len(alunos)
    print(f"A média dos alunos foi: {media:.2f}")
    for n in alunos:
        if n >= 6:
            print(n, "Passou")
        else:
            print(n, "Reprovou")
media_alunos()