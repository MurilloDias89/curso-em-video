d= int(input('Quantos dias alugado? '))
km= int(input('Percoreu quantos Km? '))

cd= 60*d
ckm= 0.15*km

print('Total a pagar: R${}'.format(cd+ckm))