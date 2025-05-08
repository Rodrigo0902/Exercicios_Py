# Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso:
# [1] somar; [2] multiplicar; [3] maior; [4] novos números; [5] sair do programa.
while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    while True:
        print("\nEscolha uma opção:")
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Mostrar o maior")
        print("[4] Digitar novos números")
        print("[5] Sair do programa")
        opcao = int(input("Opção: "))
        if opcao == 1:
            print(f"A soma de {n1} + {n2} é {n1 + n2}")
        elif opcao == 2:
            print(f"A multiplicação de {n1} * {n2} é {n1 * n2}")
        elif opcao == 3:
            maior = n1 if n1 > n2 else n2
            print(f"O maior número entre {n1} e {n2} é {maior}")
        elif opcao == 4:
            print("\nDigite os novos números:")
            break  # Sai do menu interno e volta ao início do while externo
        elif opcao == 5:
            print("Finalizando o programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")