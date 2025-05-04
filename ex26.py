# Faça um programa que leia uma frase pelo tevlado e mostre:
# (a) Quantas vezes aparece a letra "A".
# (b) Em que posição ela aparece pela primeira vez.
# (c) Em que posição ela aparece pela última vez.
frase = input("Digite uma frase: ").strip().upper()
quantidade = frase.count("A")
primeira_pos = frase.find("A") + 1  # +1 para exibir posição começando em 1
ultima_pos = frase.rfind("A") + 1
print(f"A letra 'A' aparece {quantidade} vezes.")
print(f"A primeira ocorrência está na posição {primeira_pos}.")
print(f"A última ocorrência está na posição {ultima_pos}.")