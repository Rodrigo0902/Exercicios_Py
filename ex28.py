# Escreva um programa que faça o computador "pensar"em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
nmrpc = random.randint(0, 5)
nmr = int(input("Digite um número de 0 a 5:"))
while nmr not in (0, 1, 2, 3, 4, 5):
    print("Número inválido, digite novamente.")
    nmr = int(input("Digite um número de 0 a 5:"))
if nmrpc == nmr:
    print("Parabéns, você venceu!")
else:
    print("Que pena, você perdeu.")