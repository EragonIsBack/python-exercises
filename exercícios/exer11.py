#Crie um programa que jogue pedra, papel e tesoura com o usuário

import random as r

pe = ["pedra", "papel", "tesoura"]

input = str(input("escolha algo entre pedra, papel e tesoura \n"))


if input not in pe:
    print("escolha inválida")
else:
    x = r.choice(pe)
    
    if input == x:
        print("empate")
    elif (input == "pedra" and x == "tesoura") or \
         (input == "papel" and x == "pedra") or \
         (input == "tesoura" and x == "papel"):
        print(f"Você ganhou! A escolha do programa foi: {x}")
    else:
        print(f"Você perdeu! A escolha do programa foi: {x}")