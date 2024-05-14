#ler a velocidade de um carro
velocidadeCarro = float(input('Qual a velocidade do carro em KM/h: '))
velocidadeLimiteVia = 80
valorMulta = 7

#Caso ele ultrapasse 80Km/h, Mostrar uma mensagem dizendo que foi multado

#81 = 7
#82 = 14

if velocidadeCarro > velocidadeLimiteVia:
    #Calculando a multa
    valorMultaTotal = (velocidadeCarro - velocidadeLimiteVia) * valorMulta
    print('Você esta acima da velocidade permitida por isso foi multado em: R${:.2f}'.format(valorMultaTotal))
else:
    print('Você não esta acima da velocidade permitida!!!')
