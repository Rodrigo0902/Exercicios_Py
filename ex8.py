# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
M = float(input("Insira um valor em metros:"))
cm = M * 100
mm = cm * 100
print(f"{M} Metros são {cm} centímetros e {mm} milimetros.")