#Faça um programa que leia um nome de usuário e uma senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro

nome = str(input("digite um nome \n"))
senha = str(input("digite uma senha \n"))

if nome == senha:
    while nome == senha:
        print("o nome não pode ser o igual a senha \n")
        nome = str(input("digite o nome novamente \n"))
    if nome != senha:
        print(f"nome = {nome} \n senha = {senha}")



#código sugerido pelo ChatGPT:
        
#    nome = input("Digite um nome: ")
#    senha = input("Digite uma senha: ")
#
#    while nome == senha:
#        print("O nome não pode ser igual à senha.\n")
#        nome = input("Digite o nome novamente: ")
#        senha = input("Digite uma senha: ")

#    print(f"Nome: {nome}\nSenha: {senha}")
