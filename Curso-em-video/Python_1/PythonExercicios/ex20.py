from random import choice,shuffle

a1= input('Digite o nome do primeiro aluno: ')
a2= input('Digite o nome do segundo aluno: ')
a3= input('Digite o nome do terceiro aluno: ')
a4= input('Digite o nome do quarto aluno: ')

ordem= [a1,a2,a3,a4]

shuffle(ordem)

print('A ordem é: {}'.format(ordem))