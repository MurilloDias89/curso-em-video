p= float(input('Digite seu peso(Kg): '))
a= float(input('Digite sua altura(M): '))

imc= p/a**2
print('\nIMC: {:.2f}.'.format(imc), end=' ')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida')