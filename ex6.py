# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
num = int(input("Informe um número:"))
num3 = num * 3
num2 = num * 2
numv2 = math.sqrt(num)
print(f"O dobro de {num} é {num2}, o triplo é {num3} e a raiz quadrada é {numv2}.")