a = int(input('Digite o primerio numero inteiro: '))
b = int(input('Digite o segundo numero inteiro: '))
c = int(input('Digite o tercerio numero inteiro: '))

#Verificando qual o maior

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

#Verificando o maior

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

#Entregando os resultados

print('O menor numero e: {}'.format(menor))
print('O maior numero e: {}'.format(maior))