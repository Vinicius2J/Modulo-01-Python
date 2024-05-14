peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
print('Seu indice de massa corporal e: {:.4}'.format(imc))
