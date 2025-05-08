# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
num = int(input("Informe um número:"))
print(f"Tabuada de {num}:")
for t in range(10):
    tabuada = num * (t+1)
    print(f"{num} x {t+1} = {tabuada}")