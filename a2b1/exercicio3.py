def somaNum(a, b):
    if (a + b) > 1000:
        raise OverflowError
    else:
        return a + b
try:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é igual a ', somaNum(v1, v2))
except ValueError:
    print('Valores Inválidos!!! Digite numeros inteiros')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é igual a ', somaNum(v1, v2))
except OverflowError:
    print('Valores muito altos! Digite numeros cujo a soma irá dar um valor menor que 1000')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é igual a ', somaNum(v1, v2))