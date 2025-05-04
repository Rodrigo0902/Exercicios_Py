# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cdd = input("Informe o nome de uma cidade:").upper().strip()
if cdd.startswith("SANTO"):
    print("A cidade começa com o nome Santo.")
else:
    print("A cidade não começa com o nome Santo.")