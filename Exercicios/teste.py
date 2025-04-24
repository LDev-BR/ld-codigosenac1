import time
def cronometro():
    seg = (int(input("Segundos: ")))
    while seg > 0:
        print(seg)
        seg -= 1
        time.sleep(1)
    else:
        print("Encerrado")
cronometro()