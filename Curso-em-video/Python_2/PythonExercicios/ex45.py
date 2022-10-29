from time import sleep
from random import randint
print('JOKENPÔ')

em= randint(0,2)
ej= int(input('''\nSuas opções:
   [ 0 ] Pedra
   [ 1 ] Papel
   [ 2 ] Tesoura
Escolha: '''))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)
print()

if em==ej:
    if em==0:
        print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Papel\nJogador jogou Papel\n-=-=-=-=-=-=-=-=-=-=-=\n\033[33mEMPATE\033[m')
    elif em==1:
        print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Pedra\nJogador jogou Pedra\n-=-=-=-=-=-=-=-=-=-=-=\n\033[33mEMPATE\033[m')
    else:
        print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Tesoura\nJogador jogou Tesoura\n-=-=-=-=-=-=-=-=-=-=-=\n\033[33mEMPATE\033[m')
elif em==0 and ej==1:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Pedra\nJogador jogou Papel\n-=-=-=-=-=-=-=-=-=-=-=\n\033[32mJOGADOR VENCEU\033[m')
elif em==1 and ej==2:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Papel\nJogador jogou Tesoura\n-=-=-=-=-=-=-=-=-=-=-=\n\033[32mJOGADOR VENCEU\033[m')
elif em==2 and ej==0:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Tesoura\nJogador jogou Pedra\n-=-=-=-=-=-=-=-=-=-=-=\n\033[32mJOGADOR VENCEU\033[m')
elif em==1 and ej==0:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Papel\nJogador jogou Pedra\n-=-=-=-=-=-=-=-=-=-=-=\n\033[31mJOGADOR PERDEU\033[m')
elif em==2 and ej==1:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Tesoura\nJogador jogou Papel\n-=-=-=-=-=-=-=-=-=-=-=\n\033[31mJOGADOR PERDEU\033[m')
elif em==0 and ej==2:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou Pedra\nJogador jogou Tesoura\n-=-=-=-=-=-=-=-=-=-=-=\n\033[31mJOGADOR PERDEU\033[m')
else:
    print('\033[31mERRO, tente novamente...\033[m')