# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("Informe um número:"))
n2 = float(input("Informe outro número:"))
n3 = float(input("Informe mais um número:"))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f"O maior número é {maior} e o menor é {menor}")