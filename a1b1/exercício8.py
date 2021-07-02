n = int(input("Informe um número para que se calcule o n-ésimo termo da sequência de Fibonacci: "))
termox=1
termoy=1
if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo =  termox + termoy
        termoy = termox
        termox = termo
        count += 1
    print(termo)
