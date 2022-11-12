lista= []
for p in range(1,6):
    peso= float(input('Digite o peso da {}ª pessoa: '.format(p)))
    lista.append(peso)
print('\nO maior peso é: {}\nO menor peso é: {}'.format(max(lista),min(lista)))