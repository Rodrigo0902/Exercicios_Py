# Crie um sistema de produtos utilizando dicionário e funções onde se possa adicionar, remover e listar os produtos e também mostrar o produto mais caro.
import os
import time
produtos = {
}

def adicionar_produto(produtos, nome, preco):
    novo_id = max(produtos.keys(), default=0) + 1
    produtos[novo_id] = {"nome": nome, "preco": preco}
    print(f"Produto com ID {novo_id} adicionado com sucesso.")
    
def remover_produto(produtos, id_produto):
    if id_produto in produtos:
        del produtos[id_produto]
        print(f"Produto com ID {id_produto} removido com sucesso.")
    else:
        print(f"Produto com ID {id_produto} não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("Lista de produtos:")
    for id_produto, dados in produtos.items():
        nome = dados["nome"]
        preco = dados["preco"]
        print(f"ID: {id_produto} | Nome: {nome} | Preço: R${preco:.2f}")

def produto_mais_caro(produtos):
    if not produtos:
        print("Nenhum produto cadastrado")
    else:
        id_mais_caro = max(produtos, key=lambda id_: produtos[id_]["preco"])
        return id_mais_caro, produtos[id_mais_caro]

while True:
    os.system('cls')
    print("Opções do sistema:")
    print("1 - Adicionar novo produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Obter produto mais caro ou mais barato")
    print("5 - Encerrar sistema")
    opcao = int(input())
    while True:
        if opcao not in (1, 2, 3, 4, 5):
            os.system('cls')
            print("Opção inválida, tente novamente.")
            print("Opções do sistema:")
            print("1 - Adicionar novo produto")
            print("2 - Remover produto")
            print("3 - Listar produtos")
            print("4 - Obter produto mais caro ou mais barato")
            print("5 - Encerrar sistema")
            opcao = int(input())
        else:
            os.system('cls')
            break

    if opcao == 1:
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o valor do produto: "))
        adicionar_produto(produtos, nome, preco)
        time.sleep(3)

    elif opcao == 2:
        id = int(input("Informe o ID do produto que deseja remover: "))
        remover_produto(produtos, id)
        time.sleep(3)

    elif opcao == 3:
        listar_produtos(produtos)
        time.sleep(10)

    elif opcao == 4:
        id_prod, produto = produto_mais_caro(produtos)
        print(f"O produto mais caro é '{produto['nome']}' (ID: {id_prod}) com preço R${produto['preco']:.2f}")
        time.sleep(3)
    
    elif opcao == 5:
        print("Encerrando Sistema.")
        time.sleep(3)
        os.system('cls')
        break