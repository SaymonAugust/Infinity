lista_compras = []

resposta = input("Deseja adicionar itens à lista? (s/n) ")

while resposta == 's':
    item = input("Informe o item: ")
    lista_compras.append(item)
    resposta = input("Deseja adicionar itens à lista? (s/n) ")
else:
    print("LISTA DE COMPRAS")
    for item in lista_compras:
        print(item)
        