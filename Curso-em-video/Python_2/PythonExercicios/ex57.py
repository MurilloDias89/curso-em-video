s= str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
while s != 'M' and s != 'F':
        s= str(input('Erro ao cadastrar. Tente novamente: ')).upper()
print('Cadastrado com sucesso!')