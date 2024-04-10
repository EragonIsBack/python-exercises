#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no
#período

deposito = float(input("Qual o valor do depósito inicial? \n"))
taxa = int(input("Qual o valor da taxa de juros por mês? \n"))

juros = taxa / 100
total = deposito
mes = 0
total_ganho = []

while mes < 24:
    total *= (1 + juros)
    print(f"O valor no mês {mes + 1} é: {total:.2f}")
    total_ganho.append(total)
    mes += 1

soma = sum(total_ganho) - deposito
print(f"O valor total dos ganhos é: {soma:.2f}")
