from datetime import datetime
def mostrar_data_hora():
    agora = datetime.now()
    print(agora.strftime("Hoje é dia %d/%m/%Y e agora são %H:%M:%S"))
def marcar_reuniao():
    compromisso = (input("Deseja marcar um compromisso?(s) para sim e (n) para não: "))
    if compromisso == "s":
        nome = input("Digite o nome do evento: ")
        eventodia = int(input("Digite o dia: "))
        eventomes = int(input("Digite o mês:"))
        eventoano = int(input("Digite o ano: "))
        data = (int(input(f"{nome} - {eventodia}/{eventomes}/{eventoano}")))
        print(data)
    else:
        print("Tenha um bom dia")
mostrar_data_hora()
marcar_reuniao()