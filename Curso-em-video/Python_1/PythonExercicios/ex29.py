km= int(input('Digite a velociade atual do carro em Km: '))

if km <= 80:
    print('\nTenha um Bom dia! Dirija com cuidado!')
else:
    m=7*(km-80)
    print('\nMultado! Sua multa é de R${} reais!!\nTenha um Bom dia! Dirija com cuidado!'.format(m))