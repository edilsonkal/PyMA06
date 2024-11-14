from os import system
system('cls')

try:

        x = int(input('Digite um numero:  ')) #ValueError doigitado um valo
        y = 10/x  #zeroDivisionError

        print(y)
except ValueError:
    print('Erro : VOCÊ digitou um numero invalido')
except ZeroDivisionError:
    print("Erro : Não é possivel dividir por zero   ")    
 
else: 
    print("Operação ccocluida com sucesso")    
        