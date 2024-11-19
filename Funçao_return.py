from os import system
system('cls')

#criando uma Função
def verificarPar(a):
    if(a%2==0):
        return a 
def verificarPositivo(a):
    if(a>0):
        return a
def calcularExpo(a,b):
    total = float(math.pow(a,b))
    print(f'A exponenciação entre {a} e {b} = {total}')  
#-------------------------------------------------------
valor_01 = int(input("Digite um valor:  "))
verificarPar(valor_01)
valor_02 = int(input("Digite um Valor:  "))
verificarPositivo(valor_02)  
calcularExpo(verificarPar(valor_01),verificarPositivo(valor_02))        