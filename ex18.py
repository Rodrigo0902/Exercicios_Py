# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input("Informe um ângulo:"))
cos = math.cos(ang)
sen = math.sin(ang)
tg = math.tan(ang)
print(f"O seno, cosseno e tangente deste ângulo valem respectivamente: {sen:.2f}, {cos:.2f} e {tg:.2f}")