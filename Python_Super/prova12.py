class Material:
    def __init__(self,titulo,autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        return f"{self.titulo} - {self.autor_ou_editora}"

class Livro(Material):
    def __init__(self,titulo,autor_ou_editora,genero):
        super().__init__(titulo,autor_ou_editora)
        self.genero = genero
        
    def exibir_informacoes(self):
        return super().exibir_informacoes() + f" - {self.genero}"

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora,edicao):
        super().__init__(titulo, autor_ou_editora) 
        self.edicao = edicao

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f" - {self.edicao}"

        
l1 = Livro("O sobrinho do mago","CS Lewis","blabla")
r1 = Revista("Science","um mano ai ","2ª edição")
    
print(l1.exibir_informacoes())
print(r1.exibir_informacoes())
