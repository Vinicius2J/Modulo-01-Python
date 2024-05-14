import random
nome01 = input('Primeiro aluno: ')
nome02 = input('Segundo aluno: ')
nome03 = input('Terceiro aluno: ')
nome04 = input('Quarto aluno: ')
lista = [nome01, nome02, nome03, nome04]
ordermAlunos = random.sample(lista, k=len(lista))
print('\nA orderm da apresentação será')
print('================================')
print('Primeiro aluno: {}'.format(ordermAlunos[0]))
print('Segundo aluno: {}'.format(ordermAlunos[1]))
print('Terceiro aluno: {}'.format(ordermAlunos[2]))
print('Quarto aluno: {}'.format(ordermAlunos[3]))
print('=================================')
