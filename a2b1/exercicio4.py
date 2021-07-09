n = int(input('Digite um número: '))
fat = 1
for i in range (n,1,-1):
    fat = fat*i
print('O',n,'! é igual a:',fat)
