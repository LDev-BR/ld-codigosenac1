import os

def pasta():
    pastin = os.mkdir(input("Nome da pasta: "))
    print(os.listdir("."))
pasta()