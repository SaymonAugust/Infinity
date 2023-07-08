

soma = 0

for variavel in range(0,6):
    num = int(input(f"Digite um número na posição {variavel}:  "))
    if (num%2) == 0:
        print("esse número é par")
        soma = soma + num
    else:
        print("essa variável  não é par e não entra na soma")
        
print("A soma dos números pares é: ",soma)



####################################################################


soma = 0
max_idade = 0
contador_menor_20 = 0

for variavel in range(0,3):
    print (variavel,"ª pessoa")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite M (masculino ou F (feminino): "))
    soma = soma + idade
    if idade >= max_idade:
        print("Encontramos a maior idade")
        max_idade = idade
        nome_max_idade = nome
    if (idade<20):
        contador_menor_20 = contador_menor_20 + 1


media = soma / 3
print(f"A media das idades é: {media}")
print(f"A maior idade é {max_idade} da pessoa {nome_max_idade}")
print(f"Total de pessoas menores de 20 anos é: {contador_menor_20}")
