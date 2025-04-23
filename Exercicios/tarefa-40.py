import emoji
def quiz():
    resposta = 0
    while resposta != 4:
        resposta = int(input("2 + 2 = ?: "))
    else:
        print(emoji.emojize("Parabéns :smiling_face:"))
quiz()