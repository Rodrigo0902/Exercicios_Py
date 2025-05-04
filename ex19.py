# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
nomes = []
for t in range(4):
    nome = input("Informe um nome de um aluno:")
    nomes.append(nome)
escolha = random.choice(nomes)
print(f"O aluno sorteado foi: {escolha}")