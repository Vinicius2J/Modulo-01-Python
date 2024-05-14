#Distancia em Km de uma vaigem
distanciaViagem = int(input('Qual a distacia da sua viagem em KM: '))
viagemDe200Km = 0.50
viagemDeMais200Km = 0.45

#Calcule o preço da passagem, Cobrando 0,50 por KM para vaigem de ate 200Km 

if distanciaViagem <= 200:
    valorPassagem200Km = distanciaViagem * viagemDe200Km
    print('Sua viagem e de: {}KM, por tanto você vai pagar: R${:.2f}'.format(distanciaViagem, valorPassagem200Km))
else:
    #e 0.45 para viagems mais longas
    valorPassagemMenos200Km = distanciaViagem * viagemDeMais200Km
    print('Sua viagem e de: {}KM, por tanto você vai pagar: R${:.2f}'.format(distanciaViagem, valorPassagemMenos200Km))
