# Escreva um programa para aprovar o empréstimo bancário para a compra de um casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input("Informe o valor da casa:"))
sal = float(input("Informe seu salário:"))
anos = int(input("Quantos anos irá pagar:"))
prestacao = casa / (anos*12)
trinta = sal*0.3
if trinta <= prestacao:
    print("Aprovado.")
else:
    print("Reprovado.")