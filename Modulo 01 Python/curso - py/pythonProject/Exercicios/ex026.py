frase = str(input('Digite uma frase: ')).strip()

#Qunatas vezes aparecer a letra A ?

print('A letra A aparece: {} vezes'.format(frase.lower().count('a')))

#A primeria letra A aparece na posição ?

print('A primeira letra A aparece na posição: {}'.format(frase.lower().find('a') + 1))

#A ultima letra A aparece na posiciçaõ ?

print('A ultima letra A paraece na posição: {}'.format(frase.lower().rfind('a') + 1))
