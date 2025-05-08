# Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input("Digite um número para calcular o fatorial:"))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")
