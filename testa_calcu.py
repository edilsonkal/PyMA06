from os import system

def limpar_tela():
    """Limpa o terminal."""
    system('cls' if system('') == 0 else 'clear')

def somar(a, b):
    total = a + b
    print(f"Total: {total}")

def subtrair(a, b):
    total = a - b
    print(f"Total: {total}")

def multiplicar(a, b):
    total = a * b
    print(f"Total: {total}")

def dividir(a, b):
    try:
        total = a / b
        print(f"Total: {total}")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")

def obter_valores():
    """Obtém dois valores numéricos do usuário com validação."""
    while True:
        try:
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            return a, b
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

# Loop principal
while True:
    limpar_tela()
    print("=== Calculadora ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == '5':
        print("Saindo da calculadora... Até logo!")
        break

    if opcao in ['1', '2', '3', '4']:
        valor_01, valor_02 = obter_valores()
        
        if opcao == '1':
            somar(valor_01, valor_02)
        elif opcao == '2':
            subtrair(valor_01, valor_02)
        elif opcao == '3':
            multiplicar(valor_01, valor_02)
        elif opcao == '4':
            dividir(valor_01, valor_02)
    else:
        print("Opção inválida! Escolha entre 1 e 5.")

    input("\nPressione Enter para continuar...")
