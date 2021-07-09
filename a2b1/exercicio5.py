n = int(input('Digite um numero: '))
vetor = []
i = 1
while i != n:
    cont = 0
    for j in range(1, i+1):
        if (i % j == 0)and(i!=2):
            cont = cont + 1
    if cont==2:
        vetor.append(i)
    i = i + 1
print('Os numeros primos que ficam entre 1 e ',n,'são:',vetor)