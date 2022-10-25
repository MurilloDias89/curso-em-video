c= str(input('Em que cidade tu nasceu? ')).strip()
# print(c[:5].upper() == SANTO)

c= c.lower()
c= c.capitalize()

print('Santo' in c)