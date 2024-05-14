#Faça um programa que leia a lagura e a altura de uma parede em metros calcule a sua aerea e a quantidade de tinta necessaria para pintala, sabendo que cada litro de tinta pintta um area de 2mQuandrados

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = altura * largura
litros = area / 2
print('Sua parede tem dimensão de {} x {}, A area da parede e: {} M²'.format(largura, altura, area))
print('Vai ser necessario {}l de tinta'.format(litros))
