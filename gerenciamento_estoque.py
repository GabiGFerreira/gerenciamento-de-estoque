




estoque = {
"celular": { "preco": 5000.00, "quantidade": 5},
"detergente": { "preco": 13.00, "quantidade": 50},
"brinco": {"preco": 100.00, "quantidade": 20}
}
# utilizado dicionário de dicionários pois organiza de forma bem estruturada, utilizando o nome como chave principal, acesso rápido aos dados


while True:
    print("Controle de Estoque")
    print("1 - Visualizar Estoque atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    
    escolha = input("Escolha uma opção numérica:")

    if escolha == '1': 

        for produto, info in estoque.items():
            print(f"Produto: {produto} " 
                  f" Preço: R${info['preco']:.2f} " 
                  f" Quantidade: {info['quantidade']}")
            

    elif escolha == '2':
        produto = input("Qual produto deseja adicionar?:")
        if produto in estoque:
            adicionar = int(input("Quanto deseja adicionar?:"))
            estoque[produto]["quantidade"] += adicionar
            print(f"Quantidade atualizada, totalizando {estoque[produto]["quantidade"]} unidades")

        else:
            print("Produto não encontrado.")


    elif escolha == '3':
        produto = input("Qual produto deseja retirar?:")

        if produto in estoque:
            retirar = int(input("Quanto deseja retirar? Digite um número inteiro positivo:"))

            if retirar > 0:
                if estoque[produto]["quantidade"] >= retirar:
                    estoque[produto]["quantidade"] -= retirar
                    print(f"Quantidade atualizada, totalizando {estoque[produto]["quantidade"]} unidades")
                
                else:
                    print("Quantidade à retirar superior ao estoque")

            else:
                retirar == 0
                print("Digite um número inteiro positivo. Tente novamente")
        
        else:
            print(f"Produto não encontrado.")


    elif escolha == '4':
        saida = input("Deseja sair do programa? sim/não:")
        if saida == "sim":
            break

        else:
            continue


    else:
        print("Erro, tente novamente")


    










    

      

    

