import time
def tasks():
    tasks = []
    while True:
        print('''           
            Bem vindo!''')
        escolha = input('''
        O que deseja fazer?:
        (A) - Adicionar tarefa
        (L) - Listar tarefas
        (R) - Remover tarefa (por nome)
        (S) - Sair
        Escolha: ''')
        if escolha == 'A':
            tarefa = input("Nome da tarefa: ")
            print("Adcionado com sucesso")
            tasks.append(tarefa)
            time.sleep(1)
        elif escolha == 'L':
            print(tasks)
            time.sleep(1)
        elif escolha == 'R':
            remover = input("Tarefa para remover: ")
            print("Removido com sucesso")
            tasks.remove(remover)
            time.sleep(1)
        elif escolha == 'S':
            break
        else:
            break
tasks()