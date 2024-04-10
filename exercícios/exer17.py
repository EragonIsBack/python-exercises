#Crie um programa que leia o nome e idade de várias pessoas, guardando os dados de cada
#pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) quantas
#pessoas foram cadastradas B) a média de idade C) uma lista com as mulheres D) uma lista de
#pessoas com idade acima da média

dados = []
contador = 0
soma_idades = 0

while True:
    
    nome = str(input("Digite o nome da pessoa: \n"))
    sexo = str(input("Digite o sexo da pessoa (F para feminino e M para masculino): \n"))
    idade = int(input("Digite a idade da pessoa: \n"))

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    
    soma_idades += idade
    contador += 1
    dados.append(pessoa)

    continuar = str(input("Gostaria de continuar? (s para sim ou n para não): \n"))
    
    if continuar == "n":
        print(dados)
        print(f"Pessoas cadastradas = {contador} \n")
        
        media = soma_idades / contador
        print(f"A média de idade das pessoas (suponho que aritmética) é: {media} \n")
        
        print("As pessoas femininas são: \n")
        for pessoa in dados:
            if pessoa['sexo'].upper() == 'F':
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
        
        print("\nPessoas com idade acima da média são: \n")
        for pessoa in dados:
            if pessoa['idade'] > media:
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
                
        break
