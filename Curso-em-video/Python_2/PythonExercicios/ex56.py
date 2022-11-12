mei = cont = maior = 0
nome= ''
lista= []
for a in range(1,5):
    print('----- {} PESSOA -----'.format(a))
    n= str(input('Digite o nome: '))
    i= int(input('Digite a idade: '))
    s= str(input('Digite o sexo [M/F]: ')).upper()

    mei+=i
    if s=='F':
        if i < 20:
            cont+=1
    if s=='M':
        lista.append(i)
        maior= max(lista)
        if i==maior:
            nome=n

print('\nA média das idades de todo mundo é de: {}'.format(mei/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nome))
print('Tem {} mulheres menores de 20 anos'.format(cont))