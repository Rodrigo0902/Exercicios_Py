# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nomes = []
for t in range(4):
    nome = input("Informe um nome de um aluno:")
    nomes.append(nome)
random.shuffle(nomes)
print(f"A ordem de apresentação do trabalho é: {nomes}")