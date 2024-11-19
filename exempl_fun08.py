from os import system
system('cls')

def fatorIal (n):
    if n == 0 or n == 1 :
        return 1 
    else:
        return n * fatorIal(n-1)
    
print(fatorIal(5))    