heigth = float (input('Digite sua altura: '))
gender = input ('Digite o sexo: M/F ')

if (gender == 'F','f'):
    weigth = (62.1 * heigth) - 44.7
elif (gender == 'M','m'):
    weigth = (72.7 * heigth) - 58
else:
    print('Sexo Invalido!')

print('O peso ideal é:', weigth)