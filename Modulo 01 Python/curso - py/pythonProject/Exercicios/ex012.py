produto = float(input('Digite o valor do produto: '))
des = produto * (5 / 100)
ValorTotal = produto - des
print('Preço: {:.2f} BRL! Com desconto de 5% fica, {:.2f} BRL!'.format(produto, ValorTotal))
