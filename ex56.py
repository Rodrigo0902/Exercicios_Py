# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# (a) A média de idade do grupo.
# (b) Qual é o nome do homem mais velho.
# (c) Quantas mulheres têm menos de 20 anos.
soma_idade = 0
homem_mais_velho_nome = ''
homem_mais_velho_idade = 0
mulheres_menos_20 = 0
for i in range(1, 5):
    print(f"\n--- Pessoa {i} ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1
media_idade = soma_idade / 4
print("\n=== Resultado ===")
print(f"(a) A média de idade do grupo é: {media_idade:.1f} anos")
if homem_mais_velho_nome:
    print(f"(b) O homem mais velho é {homem_mais_velho_nome} com {homem_mais_velho_idade} anos")
else:
    print("(b) Nenhum homem foi registrado.")
print(f"(c) {mulheres_menos_20} mulher(es) têm menos de 20 anos")