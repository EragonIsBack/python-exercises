#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
#quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
#números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numeros = []

while True:
    num = int(input("digite um numero (999 para sair) \n"))
    numeros.append(num)

    if num == 999:
        break

if 999 in numeros:
    numeros.remove(999)
    x = sum(numeros)

print(f"A soma total dos numeros é: {x}")
