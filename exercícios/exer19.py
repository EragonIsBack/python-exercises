#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
#usando um loop `for`

num = int(input("Digite um número: \n"))

if num <= 1:
    print("O número não é primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("O número é primo")
    else:
        print("O número não é primo")
