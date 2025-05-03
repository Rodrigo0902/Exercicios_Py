# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
km = float(input("Quantos KM foram percorridos?"))
dias = int(input("Quantos dias se passaram?"))
km = km * 0.15
dias = dias * 60
total = km + dias
print(f"O valor total da viagem ficou em {total:.2f}.")