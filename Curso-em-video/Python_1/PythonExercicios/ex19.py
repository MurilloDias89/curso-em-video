from random import choice

a1= input('Digite o nome do primeiro aluno: ')
a2= input('Digite o nome do segundo aluno: ')
a3= input('Digite o nome do terceiro aluno: ')
a4= input('Digite o nome do quarto aluno: ')

sorteio= [a1,a2,a4,a3]

print('O sorteado foi: {}'.format(choice(sorteio)))