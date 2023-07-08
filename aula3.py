soma_idade = 0
quantidade_menos_de_20 = 0
idade_mais_velha = 0
nome_mais_velha = 0

for i in range(0, 3):
    nome = input('Digite seu nome: ')
    idade = int(input('Qual sua idade:'))
    sexo = input('Digite seu sexo: M/F ')
    if idade < 20:
     quantidade_menos_de_20 = quantidade_menos_de_20 + 1
    if idade > idade_mais_velha:
     idade_mais_velha = idade
     nome_mais_velha = nome
    
    
soma_idade = soma_idade + idade



media_idade = soma_idade / 3

print('Pessoas com menos de 20 anos: ', quantidade_menos_de_20)
print('Media de idade das pessoas: ', media_idade)
print('Mais velha: ', nome_mais_velha)

print('Quantidade de pessoas com menos de 20 anos: ', quantidade_menos_de_20, ',media de idade entre as 3 pessoas: ', media_idade, 'a mais velha sendo: ', nome_mais_velha)