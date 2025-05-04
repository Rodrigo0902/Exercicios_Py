# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se
# já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input("Qal o ano de seu nascimento?"))
idade = 2025 - ano
if idade < 18:
    print(f"Ainda não precisa se alistar, falta {18 - idade} ano/os.")
elif idade == 18:
    print(f"Você precisa se alistar.")
else:
    print(f"Já deveria ter se alistado, está {idade - 18} ano/os atrasado.")