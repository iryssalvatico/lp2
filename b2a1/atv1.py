with open('bases-lp2', 'r') as arq: 
    arquivo = arq.readlines()
print (arquivo)
i = 0
while i < len(arquivo):
    z = arquivo[i]
    print(("Citosina está presente"),(z.count('C')),('vezes na'),('linha'),(i+1)) 
    print(("Guanina está presente"),(z.count('G')),('vezes na'),('linha'),(i+1))
    print(("Timina está presente"),(z.count('T')),('vezes na'),('linha'),(i+1))
    print(("Adenina está presente"),(z.count('A')),('vezes na'),('linha'),(i+1))
    print('\n\n')
    i=i+1