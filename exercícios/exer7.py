#Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar

while True:
    x = int(input(""))

    div = x%2 

    if div == 1:
        print("é impar")
    elif div == 0:
        print("é par")
