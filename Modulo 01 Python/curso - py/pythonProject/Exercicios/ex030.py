numero = int(input('Digite um numero inteiro: '))
aNumero = (numero % 2) == 0
if aNumero:
    print('O numero {} e par'.format(numero))
else:
    print('O numero {} e impar'.format(numero))
