from os import system
system ('cls')

import time
soma = 0

while (True):
    num = int(input("Digite um numero"))
    if (num <0):
        break
    soma += num 
print(f'A soma dos numeros é : {soma}')
    