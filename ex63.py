# Dado um dicionário com o total de vendas de cada vendedor:
vendas = {
    "Ana": 1200,
    "Carlos": 950,
    "Maria": 1870
}
# Crie uma função melhor_vendedor(dicionario) que retorne o nome e o valor do maior vendedor.
def melhor_vendedor(x):
    nome = max(x, key=x.get)
    valor = x[nome]
    return nome, valor

print(melhor_vendedor(vendas))