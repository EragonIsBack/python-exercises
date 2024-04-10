#Faça um programa que leia a idade de uma pessoa e informe sua classe eleitoral: não eleitor
#(abaixo de 16 anos), eleitor obrigatório (entre 18 e 65 anos) e eleitor facultativo (entre 16 e 18
#anos e maior de 65 anos)

idade = int(input("qual a sua idade?"))

if idade < 16:
    print("você não tem idade pra voltar.")
elif idade >= 18 and idade <= 65:
    print("você é obrigado a votar. ")
elif idade == 17:
    print("você tem idade pra votar como eleitor facultativo")
elif idade > 65:
    print("você tem idade pra votar como eleitor facultativo")