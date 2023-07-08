lista_compras = [
    'Arroz',
    'Açucar',
    'Farinha',
    'Macarrão',
    'Molho de Tomate'
]

for produto in lista_compras:
    print(produto)
    
resposta = input("Deseja adicionar um produto à lista? (sim/não) : ")

if resposta == "sim":
    
    produto_adicional = input("Qual produto você quer adicionar? ")
    lista_compras.append(produto_adicional) 
    
    for produto in lista_compras:
        print(produto)

else:
    for produto in lista_compras:
        print(produto)
    