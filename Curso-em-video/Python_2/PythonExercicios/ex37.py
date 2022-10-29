n= int(input('Digite um valor inteiro: '))
r= int(input("""\nEscolha uma das bases para conversão:
     [ 1 ] Binário
     [ 2 ] Octal
     [ 3 ] Hexadecimal
Sua opção: """))

if r==1:
    b= bin(n)
    print('\n{} convertido em binário é {}'.format(n,b[2:]))
elif r==2:
    o= oct(n)
    print('\n{} convertido em octal é {}'.format(n,o[2:]))
elif r==3:
    h= hex(n)
    print('\n{} convertido em hexadecimal é {}'.format(n,h[2:]))
else:
    print('\nERRO, tente novamente.')