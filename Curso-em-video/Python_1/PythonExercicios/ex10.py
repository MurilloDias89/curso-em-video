n= float(input('Digite quanto você tem na carteira: '))
dolar= float(input('Digite o dólar para converter em real: '))

d= n/5.16
dd= dolar*5.16

print('Você pode comprar {:.2f} dólares! {:.2f} em valor em real é {:.2f}!'.format(d,dolar,dd))