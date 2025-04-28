import time
def relogio_digital():
    for hora  in range(int(input("Horas para simular: "))):
        for minuto in range(60):
            for segundo in range(60):
                print(f"{hora} horas {minuto} minutos e {segundo} segundos.")
                time.sleep(1)
    print("Finalizado")
relogio_digital()