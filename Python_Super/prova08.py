from time import sleep
import os

def menu():
    """
    Função menu não recebe nada como parametro 
    Exibe um menu de opcoes interativo para que o usuari consiga escolher dinamicamente oque fazer 
    retorna a opcao escolhida na variavel 'opcao'
    """
    print("="*30)
    print("Menu Interativo".center(30))
    print("="*30)
    print("""
1 - Para Adicionar produto
2 - Para Listar produto
3 - Para Atualizar produto
4 - Para Excluir produto
5 - Para Limpar Terminal
6 - Para Sair
""")
    opcao = input("->")
    return opcao


def adicionar_produto(lista:list):
    """
    lista --> recebe um objeto da classe list , sera nossa lista desejada
    Essa função recebe como parametro uma lista e adiciona um produto nela pedindo a ele as informações como nome, quantidade,preco_unitario, e Valor_total_em_estoque e não permite adicionar um produto com o nome vazio


    """
    produto = {}
    produto["nome"] = input("Digite o nome do produto:")
    produto["quantidade"] = int(input("Digite a quantidade do produto:"))
    produto["preco_unitario"] = float(input("Digite o preco unitario do produto:"))
    produto["valor_total_em_estoque"] = produto["quantidade"]*produto["preco_unitario"]
    if produto["nome"]:
        lista.append(produto)
        print(" \033[32mProduto adicionado com sucesso \033[m")
    else:
        print("Não é possivel adicionar um produto sem nome")
        adicionar_produto(lista)


def listar_produtos(lista:list):
    """
    lista --> objeto da classe list

    Essa função itera sobre a lista recebida como parametro e logo apos itera sobre prouduto que esta dentro da lista que é representado como dicionario 

    """
    if lista:
        for produto in lista:
            for chave in produto:
                print(f"{chave}:{produto[chave]}")
            print()
    else:
        print("\033[31mNenhum produto adicionado na lista\033[m ")
        sleep(2)


def atualizar_produto(lista:list):
    """
    lista --> recebe um objeto da classe list

    
    """
    nome = input("Digite o nome do produto que voce deseja atualizar:")
    for produto in lista:
        if produto["nome"] == nome:
            
            produto["nome"] = input("Digite o nome do produto:")
            produto["quantidade"] = int(input("Digite o nome do produto:"))
            produto["preco_unitario"] = float(input("Digite o nome do produto:"))
            print("\033[32mProduto atualizado com sucesso \033[m")
        else:
            print("\033[31mErro Produto não encontrado \033[m")


def deletar_produto(lista:list):
    """
    lista --> recebe um objeto da classe list

    
    """
    nome = input("Digite o nome do produto que voce deseja Deletar:")
    for produto in lista:
        if produto["nome"] == nome:
            lista.remove(produto)
            print("\033[32mProduto deletado com sucesso \033[m")
        else:
            print("\033[31mErro Produto não encontrado \033[m")


def limpar_terminal():
    """
    Limpa o terminal atravez da lib os nativa do python 

    """
    os.system("cls")

            
lista_produtos = []
while True:
    opcao = menu()
    if opcao == "1":
        adicionar_produto(lista_produtos)
        
    elif opcao == "2":
        listar_produtos(lista_produtos)
        
    elif opcao == "3":
        atualizar_produto(lista_produtos)

    elif opcao == "4":
        deletar_produto(lista_produtos)
        
    elif opcao == "5":
        limpar_terminal()
    
    elif opcao == "6":
        print("\033[31mFinalizando...\033[m")
        sleep(3)
        break
    else:
        print("\033[31mPor favor digite uma opção valida\033[m")
        sleep(2)
