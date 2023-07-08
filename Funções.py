def calcular_imc():
    pessoas = []

    for i in range(4):
        nome = input("Digite o nome da pessoa {}: ".format(i+1))
        peso = float(input("Digite o peso (em kg) da pessoa {}: ".format(i+1)))
        altura = float(input("Digite a altura (em metros) da pessoa {}: ".format(i+1)))

        imc = peso / (altura ** 2)
        pessoa = {"Nome": nome, "Peso": peso, "Altura": altura, "IMC": imc}
        pessoas.append(pessoa)

    return pessoas

resultado = calcular_imc()

# Exibindo o resultado
for pessoa in resultado:
    print("Nome: {}".format(pessoa["Nome"]))
    print("Peso: {} kg".format(pessoa["Peso"]))
    print("Altura: {} m".format(pessoa["Altura"]))
    print("IMC: {:.2f}".format(pessoa["IMC"]))
    print()