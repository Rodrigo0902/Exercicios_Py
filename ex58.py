# Melhore o jogo do exercício 028 onde o computador vai "pensar"em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
nmrpc = random.randint(0, 10)
contador = 0
nmr = int(input("Digite um número de 0 a 10:"))
contador += 1
while nmr not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print("Número inválido, digite novamente.")
    nmr = int(input("Digite um número de 0 a 10:"))
while nmr != nmrpc:
    print("Tente novamente!")
    nmr = int(input("Digite um número de 0 a 10:"))
    while nmr not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        print("Número inválido, digite novamente.")
        nmr = int(input("Digite um número de 0 a 10:"))
    contador += 1
print(f"Você venceu com um total de {contador} tentativas!")