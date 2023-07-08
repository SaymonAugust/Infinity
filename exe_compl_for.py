
soma = 0
num_imp = ''
for variavel in range(1,101):
    if variavel %2 == 0:
       soma = soma + 1
    else:
        num_imp = num_imp + str(variavel) + ' '
        print(variavel)
        
        
print(f"Existem: {soma} números pares")
print(num_imp)



        