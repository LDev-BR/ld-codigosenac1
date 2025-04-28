def usuarios():
    users = ["Nathan", "Pedro", "Ariel", "Sigma", "Lucia"]
    question = input("Seu nome: ")
    for n in users:
        if question == n:
            print("Você está na lista")
            break
        else:
            print("Você não está na lista")
            break
usuarios()