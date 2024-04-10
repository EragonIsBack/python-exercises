#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

import random as r


x = int(input("escolha um numero de 0 a 5. \n"))
y = r.randint(0, 5)


while True:
    if x == y:
        print(f"Você acertou! O numero escolhido foi: {x}")
        break
    elif x != y:
        print(f"você errou. Tente novamente.")