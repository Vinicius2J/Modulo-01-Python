dias = int(input('Quantos dia alugados: '))
km = int(input('Quantos Km rodados:  '))
precoTotal = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(precoTotal))
