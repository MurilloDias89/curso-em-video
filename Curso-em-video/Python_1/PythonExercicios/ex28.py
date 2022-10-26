from random import randint
from time import sleep

n= randint(0,5)
a= int(input('Vou pensar em um número entre 0 e 5, tente adivinhar! '))
print('\nProcessando...')
sleep(2)

if a == n:
    print('\nParabéns, você acertou !!')
else:
    print('\nErroooou! Eu pensei no {}'.format(n))