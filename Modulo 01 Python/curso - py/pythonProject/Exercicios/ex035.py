a = float(input('Digite o comprimerio da primeira reta: '))
b = float(input('Digite o comprimerio da segunda reta: '))
c = float(input('Digite o comprimerio da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Sim e possivel forma um triangulo')
else:
    print('Não e possivel forma um triangulo')