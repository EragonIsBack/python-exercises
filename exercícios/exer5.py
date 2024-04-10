#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
#milímetros

metros = float(input("digite um valor em metros. \n"))

cm = float(100)
ml = float(1000)

convcm = metros * cm
convml = metros * ml

print(f"{metros}M é equivalente a {cm}cm e a {ml}mm")