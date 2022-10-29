v= float(input('Valor da casa: '))
s= float(input('Salário do comprador: '))
a= float(input('Quantos anos de financiamento: '))

pm= v/(a*12)
s30= s*0.3

print('\nPara pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(v,a,pm))
if pm > s30:
    print('Empréstimo negado!!')
else: 
    print('Empréstimo aprovado!!')