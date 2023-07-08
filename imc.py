weigth = float (input('Dígite seu peso:'))
heigth = float (input('Digite sua altura: '))

imc = weigth / (heigth * heigth)

if (imc < 18.5):
    print('ABAIXO DO PESO')
elif (imc >= 18.5 and 24.9):
    print('PESO IDEAL')
elif (imc >= 25.0 and 29.9):
    print('LEVEMENTE ACIMA DO PESO')
elif (imc >= 30.0):
    print ('OBESIDADE GRAU 1')