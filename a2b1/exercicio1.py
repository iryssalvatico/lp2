try:
    x = int(input('Entre com um numero: '))
    y = int(input('Entre com outro numero: '))
    print(x, '/', y, '=', x / y)
except ValueError:
    print('Valores Inválidos!!! Digite numeros inteiros')
    x = int(input('Entre com um numero: '))
    y = int(input('Entre com outro numero: '))
    print(x, '/', y, '=', x / y)
except ZeroDivisionError:
    print('Não é possivel fazer divisão por 0!!! Digite outro valor')
    x = int(input('Entre com um numero: '))
    y = int(input('Entre com outro numero: '))
    print(x, '/', y, '=', x / y)