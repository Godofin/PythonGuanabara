#Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo e todas 
# as informações possíveis sobre ele.

n = input("Digite algo:\n")

print("O tipo primitivo desse valor é: {}\n".format(type(n)))
print("É um número?: {}\n".format(n.isnumeric()))
print("É alfabético?: {}\n".format(n.isalpha()))
print("É alfanumérico?: {}\n".format(n.isalnum()))
print("Esta em maiúsculo?: {}\n".format(n.isupper()))
print("Esta em minúsculo?: {}\n".format(n.islower()))
print("Esta capitalizada?: {}\n".format(n.istitle()))

