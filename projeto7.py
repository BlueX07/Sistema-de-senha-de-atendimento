def sistema_senhas():
    normal = 0
    prioritario = 0
    opcao = 0

    while opcao != 3:
        print("1 - Atendimento normal")
        print("2 - Atendimento prioritário")
        print("3 - Encerrar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            normal += 1
            print(f"Sua senha é: N{normal:03d}")
    
        elif opcao == 2:
            prioritario += 1
            print(f"Sua senha é: P{prioritario:03d}")
    
        elif opcao != 3:
            print("Opção inválida.")
    print ("Sistema encerrado.")

sistema_senhas()
