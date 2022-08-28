#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

txt= input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(txt))
print('Tem só espaços? ',txt.isspace())
print('Esse valor é númerico? ',txt.isnumeric())
print('Esse valor é um texto? ',txt.isalpha())
print('Esse valor é alfanúmerico? ',txt.isalnum())
print('Esse valor está escrito só em maiúsculo? ',txt.isupper())
print('Esse valor está escrito só em minúsculo? ',txt.islower())
print('Esse valor é capitalizado? ',txt.istitle())