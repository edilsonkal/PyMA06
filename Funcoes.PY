from os import system
system('cls')

def verificar(a):
    if(a%2==0):
        print("É par")
    else:
        print("Não é par")
#----------------------------------------        
numero = int(input("Digite um numero: "))
verificar(numero)             