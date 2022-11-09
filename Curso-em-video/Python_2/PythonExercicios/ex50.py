par= []

for c in range(1,7):
    n= int(input('Digite o {}º valor: '.format(c)))
    if n%2==0:
        par.append(n)
print('A soma dos pares é igual a {}'.format(sum(par)))