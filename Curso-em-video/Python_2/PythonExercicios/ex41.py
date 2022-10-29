from datetime import date
i= int(input('Digite sua idade: '))

d= date.today().year
i= d-i

if i<=9:
    print('\nIdade: {}\nClassificação: MIRIM'.format(i))
elif i<=14:
    print('\nIdade: {}\nClassificação: INFANTIL'.format(i))
elif i<=19:
    print('\nIdade: {}\nClassificação: JÚNIOR'.format(i))
elif i<=25:
    print('\nIdade: {}\nClassificação: SÊNIOR'.format(i))
else:
    print('\nIdade: {}\nClassificação: MASTER'.format(i))