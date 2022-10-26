n1= int(input('Digite um valor: '))
n2= int(input('Digite um valor: '))
n3= int(input('Digite um valor: '))
 
if n1 < n2 and n1 < n3:
    me= n1
elif n2 < n3:
    me= n2
else:
    me= n3

if n1 > n2 and n1 > n3:
    ma= n1
elif n2 > n3:
    ma= n2
else:
    ma= n3

print('z\nMaior: {}\nMenor: {}'.format(ma,me))