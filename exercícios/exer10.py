#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Qual o número? \n"))

if num > 1:
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
