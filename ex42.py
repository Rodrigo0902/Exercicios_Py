# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# todos os lados iguais é EQUILÁTERO; dois lados iguais é ISÓSCELES; todos os lados diferentes é ESCALENO.
a = float(input("Informe o primeiro lado:"))
b = float(input("Informe o segundo lado:"))
c = float(input("Informe o terceiro lado:"))
if a + b > c or b + c > a or a + c > b:
    print("Esse triângulo pode existir.")
    if a == b == c:
        print("Este triângulo é EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("Este triângulo é ISÓSCELES")
    else:
        print("Este triângulo é ESCALENO")
else:
    print("Esse triângulo não pode existir.")