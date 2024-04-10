#Desenvolva um programa que leia o nome, idade de 4 pessoas. No final do programa,
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
#têm menos de 20 anos

pessoas = []
idade_homens = []
contador = 0
idades = 0

while contador < 4:
    nome = str(input("Digite um nome: \n"))
    idade = int(input("Digite a idade: \n"))
    sexo = str(input("Digite o gênero (f ou m): \n"))
    
    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    
    pessoas.append(pessoa)
    contador = contador + 1
    idades = idades + idade

    if sexo.upper() == 'M':
        idade_homens.append(idade)

med = idades/contador

print("\nPessoas do sexo feminino com menos de 20 anos:")
for pessoa in pessoas:
    if pessoa['sexo'].upper() == 'F' and pessoa['idade'] < 20:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")

homem_mais_velho = max(idade_homens)
for pessoa in pessoas:
    if pessoa['sexo'].upper() == 'M' and pessoa['idade'] == homem_mais_velho:
        print(f"\nO homem mais velho é: {pessoa['nome']}, Idade: {pessoa['idade']}")

print(f"\nA média da idade das pessoas é: {med}")
print("Acabamos :') ")
