from os import system
system('cls')
texto = "O tempo perguntou para o tempo quanto tempo o tempo tem"

print(texto.startswith("O"))
print(texto.endswith("tem"))
print("para" in texto)
print(texto.count('Tempo'))
textoTrocado =  texto.replace("tempo","horas")
print(textoTrocado)