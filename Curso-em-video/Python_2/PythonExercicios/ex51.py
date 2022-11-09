print('10 TERMOS DE UMA PA')

t= int(input('\nPrimeiro termo: '))
r= int(input('Razão: '))
d= t+(10-1)*r

for c in range(t,d+r,r):
    print(c, end=' -> ')
print('ACABOU')