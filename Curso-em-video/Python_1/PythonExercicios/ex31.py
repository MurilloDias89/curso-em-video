v= int(input('Digite a distância da sua viagem em Km: '))

if v <= 200:
    print('\nPreço da viagem: {:.2f}'.format(v*0.5))
else:
    print('\nPreço da viagem com desconto: {:.2f}'.format(v*0.45))