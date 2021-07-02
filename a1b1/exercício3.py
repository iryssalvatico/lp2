print ("Informe três números diferentes para serem ordenados de forma crescente:")
x = 0
vetor = list(range(3))
while x < 3:
    vetor [x] = int(input('Informe um número:'))
    x = x+1
vetor.sort()
print('Os números ordenados de forma crescente correspondem a: ',vetor)
