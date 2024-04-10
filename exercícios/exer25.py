#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
#podem ou não formar um triângulo

reta1 = float(input("Qual o tamanho da reta 1? \n"))
reta2 = float(input("Qual o tamanho da reta 2? \n"))
reta3 = float(input("Qual o tamanho da reta 3? \n"))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("As retas podem formar um triângulo.")
else:
    print("As retas tem tamanhos diferentes, e portanto não podem formar um triângulo.")