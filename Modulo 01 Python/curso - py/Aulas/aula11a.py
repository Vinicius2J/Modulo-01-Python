n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 7:
    print('\nSua media foi: {:.1f}'.format(m))
    print('-'*20)
    print('Voê reprovou !!!')
else:
    print('\nSua media foi: {:.1f}'.format(m))
    print('-'*20)
    print('Você passou, parabans !!!')