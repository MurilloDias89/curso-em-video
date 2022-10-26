s= float(input('Digite o salário: R$'))

if s <= 1250:
    a= s*0.15+s
else:
    a= s*0.1+s

print('\nO aumento é de: R${:.2f}'.format(a))