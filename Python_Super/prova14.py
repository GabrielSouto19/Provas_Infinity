#Projeto Python Biblioteca

#Gerenciamento de uma biblioteca

from time import sleep
import os
resetar_cor = "\033[m"
cor_vermelho = "\033[31m"
cor_verde = "\033[32m"
class Livro:
    def __init__(self,titulo,autor,id) -> None:
        self.titulo = titulo 
        self.autor = autor 
        self.id = id
        self.disponivel = True

    def __str__(self) -> str:
        return f"ID:{self.id} ---Titulo:{self.titulo} - Autor:{self.autor} ---Disponivel: {self.disponivel}"


class Membro:
    def __init__(self,nome,numero_membro) -> None:
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_livros_emprestados = []

class Biblioteca:
    def __init__(self) -> None:
        self.registro_membros = []
        self.catalogo_livros = []

    def adicionar_livro_ao_catalogo(self,livro:Livro):
        self.catalogo_livros.append((livro))
        print(f"{cor_verde}Livro adicionando com sucesso{resetar_cor}")


    
    def adicionar_membro(self,membro:Membro):
        self.registro_membros.append((membro))

    def emprestar_livro_ao_membro(self,livro:Livro,membro:Membro):
        if (membro) in self.registro_membros:
            if (livro) in self.catalogo_livros:
                if livro.disponivel == True:
                    livro.disponivel = False
                    membro.historico_livros_emprestados.append(livro)
                    print(f"{cor_verde}Livro emprestado com sucesso{resetar_cor}")


    def devolver_livro(self,livro:Livro):
        livro.disponivel = True
        print(f"{cor_verde}Livro devolvido com sucesso {resetar_cor}")

    def consultar_livros(self,titulo=None,autor=None,id=None):
        if titulo != None:
            for livro in self.catalogo_livros:
                if livro.titulo == titulo.strip():
                    return livro
                   

        
        if autor != None:
            for livro in self.catalogo_livros:
                if livro.autor == autor.strip():
                    return livro
                    

        
        if id != None:
            for livro in self.catalogo_livros:
                if livro.id == id:
                    return livro


        if titulo == None and autor == None and id == None:
            for livro in self.catalogo_livros:
                print(livro) 
            

    def consultar_membro(self,registro_membro):
        for membro in self.registro_membros:
            membro.numero_membro == registro_membro
            return membro

             


def menu():
    print("="*30)
    print("Menu Interativo".center(30))
    print("="*30)
    print("""
1 - Para adicionar Livro
2 - Para adicionar Membro
3 - Para Consultar Livro
4 - Para Consultar Membro
5 - Para Emprestar Livro
6 - Para Devolver Livro
7 - Finalizar programa
""")
    opcao= int(input("->"))
    return opcao

# l1 = Livro("O sobrinho do mago","CS Lewis",1)
# m1 = Membro("Gabriel","0001")

b1 = Biblioteca()

# print(b1.catalogo_livros)
# b1.adicionar_livro_ao_catalogo(l1)
# print(b1.catalogo_livros)
# b1.adicionar_membro(m1)

# b1.emprestar_livro_ao_membro(livro=l1,membro=m1)
# b1.consultar_livros(titulo="O sobrinho do mago")

while True:
    opcao = menu()
    if opcao == 1:
        nome = input("Digite o nome do livro:")
        autor = input("Digite o autor do livro:")
        id = input("Digite o id do livro:")
        b1.adicionar_livro_ao_catalogo(Livro(nome,autor,id))
        

    
    
    elif opcao == 2:
        nome = input("Digite o nome do membro:")
        registro = input("Digite o numero de registro:")
        b1.adicionar_membro(Membro(nome,registro))
        
    
    
    elif opcao == 3:
        titulo = input("Digite o titulo do livro que deseja buscar(deixar em branco caso não saiba):")
        autor = input("Digite o autor do livro que deseja buscar(deixar em branco caso não saiba):")
        id = input("Digite o id do livro que deseja buscar(deixar em branco caso não saiba):")
        if titulo:
            print(b1.consultar_livros(titulo=titulo))
            
       
        if autor:
            print(b1.consultar_livros(autor=autor))
            


        if id:
            print(b1.consultar_livros(id=id))
            

        if not titulo and not autor and not id:
            b1.consultar_livros()

    elif opcao == 4:
        numero_membro = input("Digite o nome numero do membro que deseja consultar:")
        print(b1.consultar_membro(registro_membro=numero_membro))
    
    elif opcao == 5:
        nome_livro = input("Digite o livro que deseja emprestar").strip()
        livro = b1.consultar_livros(titulo=nome_livro)
        registro_membro = input("Digite o numero de membro pra fazer o emprestimo")
        membro = b1.consultar_membro(registro_membro=registro_membro)
        b1.emprestar_livro_ao_membro(livro=livro,membro=membro)
    
    
    elif opcao == 6:
        nome_livro = input("Digite o nome do livro que deseja devolver")
        livro = b1.consultar_livros(titulo=nome_livro)
        b1.devolver_livro(livro=livro)
    
    
    elif opcao == 7:
        print(f"{cor_vermelho}Finalizando programa{resetar_cor}")
        sleep(1)
        break
    
    else:
        print(f"{cor_vermelho}Escolha uma opcao valida{resetar_cor}")
        sleep(1)
        os.system('cls')#atenção se caso estiverem corrigindo a prova pelo sistema operacional linux , favor trocar de cls para clear o argumento


