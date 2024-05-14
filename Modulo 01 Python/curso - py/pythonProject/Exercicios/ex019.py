import random
aluno01 = input('Digite o nome do primeiro aluno: ')
aluno02 = input('Digite o nome do segundo aluno: ')
aluno03 = input('Digite o nome do terceiro aluno: ')
aluno04 = input('Digite o nome do quarto aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]
alunoEscolhido = random.choice(lista)
print('O aluno escolhido foi o {}'.format(alunoEscolhido))
