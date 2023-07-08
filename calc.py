def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# def subtrair(a, b):
#     return a - b

subtrair = lambda a, b : a - b

# Função para exibir o menu
def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Subtrair")
    print("5 - Sair")

# Programa principal
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '5':
        print("Programa encerrado.")
        break
    
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    
    if opcao == '1':
        resultado = somar(num1, num2)
        print("Resultado da soma:", resultado)
    elif opcao == '2':
        resultado = multiplicar(num1, num2)
        print("Resultado da multiplicação:", resultado)
    elif opcao == '3':
        resultado = dividir(num1, num2)
        print("Resultado da divisão:", resultado)
    elif opcao == '4':
        resultado = subtrair(num1, num2)
        print("Resultado da subtração:", resultado)
    else:
        print("Opção inválida. Tente novamente.")
    
    print() 