import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: ')) 
hi = pow(co, 2) + pow(ca, 2)
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(hi)))
