nome= str(input('Digite o seu nome: '))

if nome=='Murillo':
    print('\nSeu nome é bem legal!')
elif nome=='Solange':
    print('\nQue nome chique!')
elif nome in 'Ewander Odirlei Juliana':
    print('\nQue nome bacana')
else:
    print('\nSeu nome é bem normal')
print('\nTenha um bom dia, {}!'.format(nome))