""""
Recebendo dados do usuario
"""

# Entrada de dados
nome = input("Qual é o seu nome? \n")
# print("Qual é o seu nome?")
# nome = input()
# Processamento

nome = nome.title()
print(f"Seja bem-vindo {nome}")

# print("Qual é a sua idade?")
# idade = input()
idade = int(input("Qual é a sua idade? \n"))
# Saída
print("%s tem %s anos de idade :)" % (nome, idade))
