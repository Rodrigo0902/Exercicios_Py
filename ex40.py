# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5,0 é REPROVADO;
# média entre 5,0 e 6,9 fica de RECUPERAÇÃO; média 7,0 ou superior é APROVADO.
n1 = float(input("Informe a primeira nota do aluno:"))
n2 = float(input("Informe a segunda nota do aluno:"))
media = (n1 + n2)/2
if media < 5:
    print("Reprovado")
elif media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")