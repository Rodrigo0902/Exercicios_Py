# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza, primeiro: Ana, último: Souza.
nome = input("Digite seu nome completo: ").strip()
nomes = nome.split()
primeiro = nomes[0]
ultimo = nomes[-1]
print(f"Primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")