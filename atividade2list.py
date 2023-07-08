lista_ingredientes1 =[
    '1/2 xícara de leite',
    '4 ovos',
    '2 e 1/2 xícaras de farinha de trigo',
    '3 cenouras',
    '2 xícaras de açucar',
    '1 colher de fermento em pó',
    '3 colheres de chocolate em pó',
    '1 xícara de leite'
]

lista_ingredientes2 = [
    '3 xícara de leite',
    '4 ovos',
    '2 e 1/2 xícaras de farinha de trigo',
    '20 morangos',
    '2 xícaras de açucar',
    '1 colher de fermento em pó',
    '5 colheres de ninho',
    '2 e 1/2 xícara de leite'
]
    
resposta = input("Deseja unir ás duas listas? (sim/não) : ")

if resposta == "sim":
    
    lista_ingredientes1.extend(lista_ingredientes2) 
    
    print("LISTAS UNIDAS")
    for item in lista_ingredientes1:
        print(item)

else:
    print("PRIMEIRA LISTA")
    for item in lista_ingredientes1:
        print(item)
    
    print()
    print()
    print()
    
    print("SEGUNDA LISTA")
    for item in lista_ingredientes1:
        print(item)