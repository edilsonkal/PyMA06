from os import system
system ('cls')

import time

print("-----------------Descobrindo o numero primo")
print("\n")
inicio = int(input("Digite o primeiro numero:   "))
fim = int(input("Digite o ultimo numero:  "))


for num in range(inicio,fim):
    primo = True
    for i in range(2,num):
        if num % i == 0:
            primo = False
            break
    if primo and num>1:
        print(f'{num} é primo ')    