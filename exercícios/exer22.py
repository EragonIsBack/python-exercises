#Desenvolva um programa que leia o nome, idade de várias pessoas. A cada pessoa
#cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas têm mais de 18 anos; B) quantos homens foram cadastrados; C) quantas
#mulheres têm menos de 20 anos

dados = []

while True:
    nome = str(input("Digite o seu nome: \n"))
    idade = int(input("Digite a sua idade: \n"))
    sexo = str(input("Digite o seu gênero: \n"))

    pessoa = {
        'nome':nome,
        'idade':idade,
        'sexo':sexo
    }

    dados.append(pessoa)

    continuar = int(input("Deseja continuar? (1 pra sim ou 0 pra não)"))
    if continuar == 0:
        break

cont_homem = 0
cont_idade = 0
cont_mulher_menor_vinte = 0
for pessoa in dados:
    if pessoa['sexo'].upper() == "M":
        cont_homem += 1
    if pessoa['idade'] > 18:
        cont_idade += 1
    if pessoa['sexo'].upper() == "F" and pessoa['idade'] < 20:
        cont_mulher_menor_vinte +=1

print(f"{cont_idade} pessoas têm mais de 18 anos")
print(f"Foram cadastrados {cont_homem} homens")
print(f"{cont_mulher_menor_vinte} têm menos de 20 anos e são do sexo feminino.")