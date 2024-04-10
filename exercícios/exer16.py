#Faça um programa que leia nome e média de um aluno, guardando também a situação
#(aprovado/reprovado) em um dicionário

situação = []

nome = str(input("qual o nome do aluno? \n"))
média = float(input("qual a média do aluno? "))
situação.append(nome)


valor_max = int(100)
valor_min = int(0)

if média >= valor_max or média < valor_min:
    print("média inválida. \n")
else:
    if média >= 60:
        situação.append(média)
        situação.append("passou")
    elif média < 60:
        situação.append("reprovou")
        situação.append(média)

    print(situação)