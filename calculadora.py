opc = int(input("""Escolha uma opção:
1 - Soma
2 - Subtração
3 - Divisão
4 - Multiplicação """))

if opc == 1:
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    resultado = x+y
    print(f'O resultado da soma entre {x} e {y} é {resultado}')
elif opc == 2:
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    resultado = x-y
    print(f'O resultado da subtração entre {x} e {y} é {resultado}')
elif opc == 3:
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    resultado = x/y
    print(f'O resultado da divisão entre {x} e {y} é {resultado}')
elif opc == 4:
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))
    resultado = x*y
    print(f'O resultado da multiplicação entre {x} e {y} é {resultado}')
else:
    print('Opção inválida')