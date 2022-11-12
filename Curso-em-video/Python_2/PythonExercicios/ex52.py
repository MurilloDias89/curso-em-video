n= int(input('Digite um número: '))

coe= n//2
val= True

for cont in range(2,coe+1):
    if n%coe==0:
        val= False
if val==True:
    print('\nO número é primo')
else:
    print('\nO número não é primo')