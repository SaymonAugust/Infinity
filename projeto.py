import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:    
    tentativa = int(input("Tente adivinhar o número: "))
    tentativas += 1    
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break    
    elif tentativa < numero_secreto:
        print("O número é maior. Tente novamente.")
    else:        
        print("O número é menor. Tente novamente.")
        print("Número adivinhado:", numero_secreto)
        print("Tentativas:", tentativas) 