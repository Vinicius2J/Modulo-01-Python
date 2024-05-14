#Solicite ao usuário o salário atual e o percentual de aumento.
salario = float(input('Digite o valor do salario atual: '))
percentual_de_aumento = int(input('Quantos % vai aumentar o salario do mesmo: '))

#Calcule o valor do aumento e o novo salário após o aumento.
aumento = salario * (percentual_de_aumento / 100)
salari_final = salario + aumento

#Exiba ambos os valores formatados adequadamente.
print('O salario do mesmo era: R${}, Com o aumento de {}%, Fica no total R${}'.format(salario, percentual_de_aumento, salari_final))    
