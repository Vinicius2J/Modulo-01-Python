#seno = Cateto Oposto / Hipotenusa
#coss = Cateto Adjacente / Hipotenusa
#tang = Cateto Oposto / Cateto Adjacente

import math
agu = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(agu))
coss = math.cos(math.radians(agu))
tang = math.tan(math.radians(agu))
print('O ângulo de {} tem o SENO de {:.2f}'.format(agu, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(agu, coss))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(agu, tang))
