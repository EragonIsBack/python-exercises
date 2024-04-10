#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
#perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta

import random as r

jogos = int(input("Quantos jogos serão gerados? \n"))

lista_numeros = []
for _ in range(jogos):
    num_sorteios = []
    for _ in range(6):
        num = r.randint(1,60)
        while num in num_sorteios:
            num = r.randint(1,60)
        num_sorteios.append(num)
    lista_numeros.append(num_sorteios)
    
for jogo in lista_numeros:
    print(jogo)