# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
catop = float(input("Qual o valor do cateto oposto?"))
catad = float(input("Qual o valor do cateto adjacente?"))
hip = math.sqrt((catop * catop) + (catad * catad))
print(f"A hipotenusa vale {hip}")