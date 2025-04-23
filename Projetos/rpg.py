def npcs():
    #Educação em primeiro lugar sempre
    print('''Bem vindo ao Gerador de NPCs''')
    #Lista de dados dos NPCs
    npc = []
    #Loop de NPCs
    for x in range(int(input('Digite o  número de npcs a serem criados: '))):
        nome = input('Nome do NPC: ')
        raca = str(input("Raça do NPC: "))
        classe = input("Classe do NPC: ")
        nvl = int(input('Nível do NPC: '))
        hp = int(input("HP do NPC: "))
        backstory = input("Origem do NPC: ")
        print('Cadastrado')
        infos = (nome, raca, classe, nvl, hp, backstory)
        npc.append(infos)
    print(f'''NPCs criados: {len(npc)}
''')
    #impressão dos NPCs
    for n in npc:
        nome = n[0]
        raca = n[1]
        classe = n[2]
        nvl = n[3]
        hp = n[4]
        backstory = n[5]
        print(f'''Nome: {nome}, raça: {raca}, classe: {classe} LVL: {nvl}, HP: {hp}, Origem: {backstory} 
''')
npcs()