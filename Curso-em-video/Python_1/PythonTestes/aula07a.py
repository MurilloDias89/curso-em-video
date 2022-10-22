n1= int(input('Digite o número 1: '))
n2= int(input('Digite o número 2: '))

s= n1+n2
sub= n1-n2
mult= n1*n2
div= n1/n2
divi= n1//n2
exp= n1**n2

print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é de {}'.format(s,sub,mult,div), end=' >>> ')
print('A divisão inteira é {} e a potência é {}'.format(divi,exp))