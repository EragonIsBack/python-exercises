#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
#aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores
#ou iguais, o aumento é de 15%

salario = int(input("qual o salario? \n"))
aumento = 0
resultado = 0

if salario > 1250:
    aumento = salario * 0.10
    resultado = salario + aumento
    print(resultado)
elif salario <= 1250:
    aumento = salario * 0.15
    resultado = salario + aumento
    print(resultado)

    