#Faça um programa que leia um número qualquer e mostre o seu fatorial

import math as m

x = int(input("digite um numero pra saber o seu fatorial. \n"))
y = m.factorial(x)

print(f"{x}! = {y}")