from os import system
system('cls')

def somar(a,b):
    total = a+b
    print("Total: ",total)
def subtrair(a,b):
    total = a-b
    print("Total : ",total) 
def multiplicar(a,b):
    total = a*b
    print("Total : ",total) 
def dividir(a:float,b:float):
    try:
        total = a/b
        print("Total : ",total) 
    except:
        print("Erro na divisão")    
#--------------------------------------------
valor_01 = int(input("Digite um valor:  "))
valor_02 = int(input("Digite um Valor:  "))  
somar(valor_01,valor_02)  
subtrair(valor_01,valor_02)
multiplicar(valor_01,valor_02)    
dividir(valor_01,valor_02)   