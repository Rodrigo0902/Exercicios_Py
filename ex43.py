# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, onde:
# abaixo de 18,5 é ABAIXO DO PESO; entre 18.5 e 25 é PESO IDEAL; 25 até 30 é SOBREPESO; 30 até 40 é OBESIDADE; acima de 40 é OBESIDADE MÓRBIDA.
peso = float(input("Informe seu peso (Em quilos):"))
alt = float(input("Informe sua altura (Em metros):"))
imc = peso (alt * alt)
if imc < 18.5:
    print("Você está ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Você está no PESO IDEAL")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO")
elif 30 <= imc < 40:
    print("Você está com OBESIDADE")
else:
    print("Você está com OBESIDADE MÓRBIDA")