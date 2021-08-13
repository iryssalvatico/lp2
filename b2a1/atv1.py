with open('bases-lp2', 'r') as arq: 
    arquivo = arq.readlines()
for i in range(0, len(arquivo), 1):
    z = arquivo[i]
    print(("Citosina está presente"),(z.count('C')),('vezes na'),('linha'),(i+1)) 
    print(("Guanina está presente"),(z.count('G')),('vezes na'),('linha'),(i+1))
    print(("Timina está presente"),(z.count('T')),('vezes na'),('linha'),(i+1))
    print(("Adenina está presente"),(z.count('A')),('vezes na'),('linha'),(i+1))
    print('\n\n')