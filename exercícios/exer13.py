#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
#que forem pares. Se o valor digitado for ímpar, desconsidere-o

import math as mt

x =  []
p1 = int(input("digite um nunero (1 de 6): \n"))
p2 = int(input("digite um nunero (2 de 6): \n"))
p3 = int(input("digite um nunero (3 de 6): \n"))
p4 = int(input("digite um nunero (4 de 6): \n"))
p5 = int(input("digite um nunero (5 de 6): \n"))
p6 = int(input("digite um nunero (6 de 6): \n"))

x.append(p1)
x.append(p2)
x.append(p3)
x.append(p4)
x.append(p5)
x.append(p6)

resultados = []

for num in x:
    if num%2 == 0:
        resultados.append(num)
    else:
        pass

soma = sum(resultados)

print(soma)

print("o código ficou longo mas It is what it is.")