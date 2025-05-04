# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 pra binário; 2 para octal; 3 para hexadecimal.
num = int(input("Informe um número:"))
print("Qual será a base de conversão?")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
decisao = int(input())
while decisao not in (1, 2, 3):
    print("Decisão inválida, informe novamente.")
    decisao = int(input())
if decisao == 1:
    num = bin(num)
elif decisao == 2:
    num = oct(num)
else:
    num = hex(num)
print(num)