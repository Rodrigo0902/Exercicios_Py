# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pequena pausa de 1 segundo entre eles.
import os
import time
for i in range(10):
    time.sleep(1)
    os.system('cls')
    print("Contagem regressiva para os fogos:")
    print(f"{10 - i}")
os.system('cls')
print("POW POW POW BOOM BOOM BOOM PFIIU PFFFIUUUUUUU")