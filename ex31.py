# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
km = int(input("Quantos KM terá a viagem?"))
if km <= 200:
    valor = km*0.5
    print(f"A viagem custará: {valor}")
else:
    valor = km*0.45
    print(f"A viagem custará: {valor}")