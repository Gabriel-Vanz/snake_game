from time import localtime, strftime
import random

def Log(nome, email):
    dataAtual = strftime("%Y-%m-%d %H:%M:%S", localtime())
    arquivo = open("Log-Snake.txt", "a")
    arquivo.write(f"Data: {dataAtual} - Nome: {nome} - E-mail: {email}\n")
    arquivo.close()

#Verifica Colisão
def Collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#Faz a randomização e o surgimento dentro do grid
def Randomize():
    x = random.randint(0,39)
    y = random.randint(0,39)
    return (x * 10, y * 10)