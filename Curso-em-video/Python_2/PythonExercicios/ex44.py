print('{:=^40}'.format(' LOJAS PH0ENIX '))

v= float(input('Valor das compras: R$'))
o= int(input('''\nFORMAS DE PAGAMENTO
   [ 1 ] à vista dinheiro/cheque
   [ 2 ] à vista no cartão
   [ 3 ] 2x no cartão
   [ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if o==1:
    d= v-v*0.1
    print('\nSelecionado à vista e o total deu {:.2f} reais com desconto de 10%'.format(d))
elif o==2:
    d= v-v*0.05
    print('\nSelecionado à vista no cartão e o total deu {:.2f} reais com desconto de 5%'.format(d))
elif o==3:
    print('\nSelecionado 2x no cartão e o total deu 2 parcelas de {:.2f} reais'.format(v/2))
elif o==4:
    p= int(input('Quantas parcelas? '))
    j= v+v*0.2
    print('\nSelecionado 3x ou mais no cartão e o total de {:.2f} reais deu {} parcelas de {:.2f} reais com 20 porcento de juros'.format(j,p,j/p))
else:
    print('\n\033[31mERRO, tente novamente...\033[m')