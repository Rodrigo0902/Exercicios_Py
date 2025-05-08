# Desenvolva um programa que leia o primeiro termo e a razão e uma PA. No final, mostre os 10 primeiros termos dessa progressão.
pt = float(input("Informe o primeiro termo da P.A.:"))
rz = float(input("Informe a razão da P.A.:"))
for i in range(10):
    i = i + 1
    termo = pt + ((i - 1)*rz)
    print(termo)