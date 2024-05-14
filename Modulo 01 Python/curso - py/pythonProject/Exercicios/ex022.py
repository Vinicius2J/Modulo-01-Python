nome = str(input('Digite seu nome: '))
#Nome para maisculas
print('Seu nome em maisculas é {}'.format(nome.upper()))

#Nome para minusculas
print('Seu nome em minusculas é {}'.format(nome.lower()))

#Tamanho do nome em letras
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#Falar o primeiro nome e seu tamanho
primerioNomeLista = nome.split()[0] 
primerioNome = primerioNomeLista

print('Seu primeiro nome é {} e ele tem {} letras'.format(primerioNome.strip(), len(primerioNome.strip())))
