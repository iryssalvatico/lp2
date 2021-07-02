palavra =  str(input('Informe uma palavra: '))
contrário = (palavra[::-1])
if palavra == contrário:
   print('Esta palavra é considerada um palíndromo')
else:
   print('Esta palavra não é considerada um palíndromo')