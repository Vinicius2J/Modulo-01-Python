numero = int(input('Digite um numero: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

#Unidade
print('Unidade: {}'.format(u))

#Dezena
print('Dezena: {}'.format(d))

#Centena
print('Centena: {}'.format(c))

#Milhar
print('Milhar: {}'.format(m))
