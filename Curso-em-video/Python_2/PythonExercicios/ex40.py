n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))

m= (n1+n2)/2

if m<5:
    print('\nREPROVADO!')
elif m >= 5 and m < 7:
    print('\nRECUPERAÇÃO!')
else:
    print('\nAPROVADO!!!')