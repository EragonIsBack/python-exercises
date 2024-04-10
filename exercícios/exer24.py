#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
#pessoas ainda não atingiram a maioridade e quantas já são maiores

idades = []
for _ in range(7):
    idade = int(input("Qual o seu ano de nascimento? \n"))
    idades.append(idade)


maior = 0
menor = 0

for idade in idades:
    if 2024 - idade > 18:
        maior += 1
    elif 2024 - idade < 18:
        menor += 1

print(f"{maior} pessoas são maiores de 18 anos.")
print(f"{menor} pessoas tem menos de 18 anos. ")