from datetime import date
cma = cme = 0
amaq= date.today().year

for a in range(1,8):
    ano= int(input('Digite o ano da {}ª pessoa: '.format(a)))
    if 18 > amaq-ano:
        cme+=1
    else:
        cma+=1

print('\nSão {} pessoa(s) que são maiores de idade\nSão {} pessoa(s) menores de idade'.format(cma,cme))