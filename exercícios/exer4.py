#Desenvolva um script que pergunte a quantidade de km percorridos por um carro alugado
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço
#a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input("quantos km o carro rodou? \n"))
dias = float(input("por quantos dias o carro foi usado? \n"))

diaria = 60
quilometro = 0.15
 
preçokm =int(km * quilometro)
preçodias = int(dias * diaria)

resultado = int
resultado = preçodias + preçokm

print(f"o valor total é: {resultado}")