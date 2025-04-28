def cursos():
    manha = {
        "Filosofia","Geografia","Quimica","Fisica"
    }
    noite = {
        "Geografia","Inglês","Espanhol","Python"
    }
    inter = manha.intersection(noite)
    print("Cursos disponiveis pela manhã: ", )
    for curso in manha:
        print(f"- {curso}\n")
    print("Cursos disponiveis pela noite: ", )
    for curso in noite:
        print(f"- {curso}\n")
    print("Cursos disponiveis nos dois periodos: ")
    for curso in inter:
        print(f"- {curso}\n")
    print("Cursos disponiveis somente na manhã: ")
    for curso in (manha - noite):
        print(f"- {curso}\n")
    print("Cursos disponiveis somente na noite: ")
    for curso in noite - manha:
        print(f"- {curso}\n")

cursos()