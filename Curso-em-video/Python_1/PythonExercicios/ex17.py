from math import hypot

co= float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(hypot(co,ca)))