import copy

estoque =[["Teclado",15]
          ,["Mouse",40]
          ,["webcam",12],
          ["Headset",25],
          ["Mousepad",50]
          ,["Cabo HDMI",30]]



estoque_original= copy.deepcopy(estoque)

opcao=-1

while opcao !=0:
    print("\n" + "=" * 50)
    print("    SISTEMA DE CONTROLE DE ESTOQUE")
    print("1-  Consultar estoque atual")
    print("2-  Consultar estoque inicial")
    print("3-  Cadastrar novo produto")
    print("4-   Inserir produto em posição especifica")
    print("5-  Atualizar quantidade de um produto")
    print("6-  Remover produto")
    print("7-  Retira último item do estoque")
    print("8-  Localizar produto e sua posição")
    print("9-  Exibir indicadores do estoque ")
    print("10- Listar produtos com estoque critico")
    print("0-  encerrar sistema")
    print("=" * 50)


    opcao= int(input("escolha sua opção: "))

    if opcao == 1:
        print("\n ESTOQUE ATUAL ")
        for i ,(prod,qtd) in enumerate(estoque):
            print(f"{i+1} - {prod} -> Quantidade :{qtd}")

    elif opcao == 2:
        print("\n ESTOQUE INICIAL ")
        for i ,(prod,qtd) in enumerate(estoque_original):
            print(f"{i+1} - {prod} -> Quanridade inicial : {qtd}")


    elif opcao == 3 :
        print("\n CADASTRAR NOVO PRODUTO ")
        prod=input("digite o nome do produto:" )
        qtd=int(input("digite a quantidade do produto : "))
        estoque.append([prod,qtd])
        print(estoque[-1])
        print("produto cadastrado com sucesso!")


    elif opcao == 4:
         print("\n INSERIR EM POSIÇÃO DE DESTAQUE ")
         prod=input("digite o nome do produto:" )
         qtd=int(input("digite a quantidade do produto : "))
         pos=int(input("digite em qual posição vc deseja inserir o produto: "))
         estoque.insert(pos,[prod,qtd])
         print(f"produto : {estoque[pos][0]} na posição {pos}")


    elif opcao == 5:
          print("\n ATUALIZAR QUANTIDADE EM ESTOQUE")
          produto=input("digite o nome do produto: ")
          encontrado= False 
          for i,(prod,qtd) in enumerate(estoque):
              if produto.lower() in prod.lower():
                  qtd_nv= int(input("digite a quantidade nova do produto: "))

                  estoque[i][1]=qtd_nv

                  print(f"produto - {prod} , Quantidade - {qtd_nv}")

          if not encontrado:
                  print("produto não encontrado")


    elif opcao == 6 :
           produto=input("digite o nome do produto: ")
           encontrado= False 
           for i, (prod, qtd) in enumerate(estoque):
            if produto.lower() in prod.lower():
                del estoque[i]
                print(f"Produto {prod} removido com sucesso")
                encontrado= True

           if not encontrado:
               print("produto não encontrado")
                  

    elif opcao == 7:
        print("\n REMOVENDO O ÚLTIMO ITEM DA LISTA DE PRODUTOS...")
        print(f"produto:{estoque[-1][0]} sendo removido")
        estoque.pop(-1)
        print("\n" + "=" * 50)
        for i ,(prod,qtd) in enumerate(estoque):
            print(f"{i+1} - {prod} -> Quantidade :{qtd}")

        print("\n" + "=" * 50)


    elif opcao == 8:
         print(f"LOCALIZAR PRODUTO E SUA POSIÇÃO")
         produto=input("digite o produto que vc deseja saber a posição: ")
         encontrado = False 
         for i,(prod,qtd) in enumerate(estoque):
             if produto.lower()==prod.lower():
                 print(f"produto na posição {i}")
                 encontrado= True


         if not encontrado:
             print("posição inexistente")
        
             


        
              
        
         
                
                
