a= float(input('Primeiro segmento: '))
b= float(input('Segundo segmento: '))
c= float(input('Terceiro segmento: '))

if a+b > c and a+c > b and b+c > a:
    if a==b==c:
        print('\nPodem formar um triângulo do tipo equilátero.')
    elif a!=b!=c!=a:
        print('\nPodem formar um triângulo do tipo escaleno.')
    else:
        print('\nPodem formar um triângulo do tipo isósceles.')
else:
    print('\nNão pode formar um triângulo!!')