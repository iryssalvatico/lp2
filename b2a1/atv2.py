from os import replace
with open('bases-lp2', 'r') as arq: 
    arquivo = arq.readlines()
print (arquivo)
i=0
while i < len(arquivo):
    z = arquivo [i]
    k1 = z.replace("A","t")
    k2 = k1.replace("T","a")
    k3 = k2.replace("G","c")
    k4 = k3.replace("C","g")
    print('\n')
    print(('Linha'),(i+1),('inicial: '),(z))
    print(('Transcrição final'),(i+1),(':'),(k4.upper()))
    i=i+1