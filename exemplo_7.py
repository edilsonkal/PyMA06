from os import system
system('cls')

def media(lista):
    return sum(lista)/len(lista) if lista else 0 

notas =[7.8.9.10]
print(media(notas))