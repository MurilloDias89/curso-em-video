soma= 0
c= 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        soma+=cont
        c+= 1
print('A soma dos {} valores é de {}'.format(c,soma))