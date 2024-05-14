#Pergunte o salario de um funcionario
salario = float(input('Digite seu salario R$: '))
salarioAcima1200 = 10
salarioAbaixo1200 = 15

#Calcule o valor de seu aumento
if salario >= 1200:
    #Para salario superiores a 1200 calcule com um aumetno de 10%
    aumento = salario * (salarioAcima1200 / 100)
    salarioAtual1200 = salario + aumento
    print('Seu salario era de: {:.2f} e com o aumento de 10%, fica: {:.2f}'.format(salario, salarioAtual1200))
else:
    #Para salario inferiores ou iguais o aumento e de 15%
    aumetnoMenos1200 = salario * (salarioAbaixo1200 / 100)
    salaroiAtualAbaixo1200 = salario + aumetnoMenos1200
    print('Seu salario era de: {:.2f} e com o aumento de 15%, fica: {:.2f}'.format(salario, salaroiAtualAbaixo1200))
