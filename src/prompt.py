import platform

from commands import *

# prompt
comando = ""
while comando != "exit":
    comando = input("/> ")

    if comando == "dir":
        dir(comando)
    elif comando != "exit":
        print("Comando Invalido!")
