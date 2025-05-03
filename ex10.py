# Crie um programa que leia quanto dinheiro uma pessoas tem na carteira e mostre quantos dólares ela pode comprar. Considere U$$1,00 = R$3,37.
real = float(input("Informe quantos reais você possui na carteira:"))
dolar = real / 3.37
print(f"Você pode comprar {dolar} dólares.")