from os import system
system('cls')

#definido as funções
def inverter_string(s):
    if len(s) == 0:
        return s 
    else:
        return s[-1]+ inverter_string(s[:-1])
palavra = input("Digite uma palavra: ")    
print(inverter_string(palavra))    