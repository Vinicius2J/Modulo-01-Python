#Digite seu nome completo

nome = str(input('Digite seu nome completo: ')).strip().split()

#Pegar informações do nome da pessoa
primerioNome = nome[0]
ultimoNome = nome[-1]

#Mensagem de boas vindas
print('Muito prazer em te conhecer!')

#Mostara o primeiro nome
print('Seu primerio nome é: {}'.format(primerioNome))

#Mostara o ultimo nome
print('Seu ultimo nome é: {}'.format(ultimoNome))
