# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = []
for i in range(1, 6):
    ano = int(input(f"Informe o ano de nascimento da {i}° pessoa:"))
    idade = 2025 - ano
    if idade > 18:
        maior.append(idade)
n = len(maior)
print(f"O número de maiores de idade foi {n}")