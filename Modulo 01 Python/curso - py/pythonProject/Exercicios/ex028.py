from random import randint
from time import sleep

#escolhendo um numero aleatorio de 0 a 5
numeroAleatorio = randint(0,5)

#Usuairo digitar qual o numero que ele acha
print('Vou pensar em um numero de 0 a 5 tente adivinhar...')
print('-=-' * 20)
numero = int(input('\nDigite um numero inteiro de 0 a 5: '))


#Fazendo a logica para ver se o ususario acertou o numero ou não
print('Processando...')
sleep(2)
if numero == numeroAleatorio:
    print('Parabens! Você acertou, numero {}'.format(numero))
else:
    print('Você perdeu! Numero aleatorio: {}, Numero digitado: {}'.format(numeroAleatorio, numero))
