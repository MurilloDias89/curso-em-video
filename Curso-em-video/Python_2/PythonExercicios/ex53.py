frase= str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= ''
for p in range(len(junto)-1,-1,-1):
    inverso+= junto[p]
if inverso==junto:
    print('\nA frase é um palíndromo!') 
else:
    print('\nA frase não é um palíndromo')