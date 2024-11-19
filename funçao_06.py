from os import system

def limpar_tela():
    """Limpa o terminal."""
    system('cls' if system('') == 0 else 'clear')

def maior_numero(lista):
    return max(lista)
numero = [1,2,3,99,23] 
print(maior_numero(numero))   
    