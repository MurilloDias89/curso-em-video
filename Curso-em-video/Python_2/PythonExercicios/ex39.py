from datetime import date

a= int(input('Digite seu ano de nascimento guerreiro: '))

d= date.today().year
r= d-a

if r==18:
    print('\nQuem nasceu em {} tem {} em {}.'.format(a,r,d))
    print('Precisa fazer o alistamento IMEDIATAMENTE!')
elif r > 18:
    print('\nQuem nasceu em {} tem {} em {}.'.format(a,r,d))
    print('Você já deveria ter se alistado há {} anos.'.format(r-18))
    print('Seu alistamento foi em {}.'.format(d-(r-18)))
else:
    print('\nQuem nasceu em {} tem {} em {}.'.format(a,r,d))
    print('Ainda faltam {} anos para você se alistar.'.format((18-r)))
    print('Seu alistamento será em {}.'.format((18-r)+d))