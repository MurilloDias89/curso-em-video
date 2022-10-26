a= float(input('Digite o primeiro segmento: '))
b= float(input('Digite o segundo segmento: '))
c= float(input('Digite o terceiro segmento: '))

if a+b > c and b+c > a and a+c > b:
    print('\nPODE formar um triângulo')
else:
    print('\nNÃO PODE formar um triângulo')