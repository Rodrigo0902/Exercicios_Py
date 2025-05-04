# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
km = int(input("Informe a velocidade do carro:"))
if km <= 80:
    print("Você não foi multado, está dentro do limite.")
else:
    valor = (km-80)*7
    print(f"Você está acima do limite! Será multado em {valor} reais.")