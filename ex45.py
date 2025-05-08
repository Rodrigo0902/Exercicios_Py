# Crie um programa que faça o computador jogar JOKENPÔ com você.
import random
ia = random.randint(1, 3)
jokenpo = input("Pedra, papel ou tesoura?").upper()
while jokenpo not in ('PEDRA', 'PAPEL', 'TESOURA'):
    print("Escolha inválida.")
    jokenpo = input("Pedra, papel ou tesoura?").upper()
if jokenpo == 'PEDRA':
    hmn = 1
elif jokenpo == 'PAPEL':
    hmn = 2
elif jokenpo == 'TESOURA':
    hmn = 3
if ia == hmn:
    print("Empate!")
elif ia == 1 and hmn == 3:
    print("A I.A. Venceu!")
elif ia == 2 and hmn == 1:
    print("A I.A. Venceu!")
elif ia == 3 and hmn == 2:
    print("A I.A. Venceu!")
elif hmn == 1 and ia == 3:
    print("Você Venceu!")
elif hmn == 2 and ia == 1:
    print("Você Venceu!")
elif hmn == 3 and ia == 2:
    print("Você Venceu!")