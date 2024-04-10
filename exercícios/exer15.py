#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os
#(com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá
#também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
#anos a pessoa vai se aposentar

#array de informações
informacoes = []

#variáveis
nome = str(input("Qual o seu nome? \n"))
ano_nascimento = int(input("qual o ano do seu nascimento? \n"))
sexo = str(input("qual o seu gênero? (Feminino/Masculino, qualquer outro será recusado.) \n"))
CTPS = int(input("qual a sua CTPS? \n"))

#mais variáveis pras verificações e cálculos serem possíveis
feminino = 'feminino'
masculino = 'masculino'
Feminino = 'Feminino'
Masculino = 'Masculino'
aposentadoriaHomem = 65
aposentadoriaMulher = 62

#jogando as informações na array
informacoes.append(nome)
informacoes.append(ano_nascimento)
informacoes.append(sexo)

#verifica se a CTPS é maior que 0, e se for joga ela na array também
if CTPS > 0:
    informacoes.append(CTPS)    

#calculo da idade
idade = 2024 - ano_nascimento 

#calculo do tempo de aposentadoria
if sexo == Feminino or sexo == feminino and CTPS > 0:
    resultado = aposentadoriaMulher - idade
    tempo = f'ainda faltam {resultado} anos para você se aposentar'
    informacoes.append(tempo)

elif sexo == Masculino or sexo == masculino and CTPS > 0:
    resultado = aposentadoriaHomem - idade
    tempo = f'ainda faltam {resultado} anos para você se aposentar'
    informacoes.append(tempo)
elif sexo == Feminino or sexo == feminino and idade >= 62:
    tempo = print("Você já tem idade para se aposentar")
    informacoes.append(tempo)
elif sexo == Masculino or sexo == masculino and idade >= 65:
    tempo = print("você já tem idade para se aposentar")
    informacoes.append(tempo)

#mostra a array de informações contendo os dados do usuário depois do "cadastro"
print(informacoes)
print(" \n Não, não foi o ChatGPT quem gerou esse código, foi eu, e sim eu comentei o meu código inteiro na mão.")