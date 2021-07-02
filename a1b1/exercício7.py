print('Informe os numeros para que se calcule a media (a media será calculada quando o valor 0 for informado')
laço = int(input('Informe um número: '))
n=0
soma = 0
while laço != 0:
    soma = soma + laço
    laço = int(input('Informe um número: '))
    n=n+1
print('A média dos números informados corresponde a: ', soma/n)