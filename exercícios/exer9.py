#Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão
#Aritmética), mostrando os 10 primeiros termos da progressão usando a estrutura for

razao = float(input("qual a razão da PA? \n"))
termo = float(input("qual o primeiro termo da PA? \n"))
n = 0

print("os 10 primeiros termos da PA são: \n")
for n in range(10):
    termo = razao + (n * razao)
    print(termo)