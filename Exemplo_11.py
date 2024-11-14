from os import system
system('cls')


lista = [1,2.3]

try:
    print(lista[3])
except IndexError:    
    print("Erro: Indice fora do intervalo")