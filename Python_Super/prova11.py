class Elevador:
    def __init__(self,totalCapacidade,atualCapacidade=0,totalAndar=0,atualAndar=0):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    
    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar+=1
            return "Subindo..."
        else:
            return "Ja estamos no topo"
    
    
    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -=1
            return "descendo"
        else:
            return "Ja estamos no terreo"
    
    
    def entrar(self,Numeropessoas:int):
        if self.atualCapacidade + Numeropessoas < self.totalCapacidade:
            self.atualCapacidade += Numeropessoas
            return "Entrando.. (la ele )"
        else:
            return("Perdão ! elevaodor cheio")


    def sair(self,numeroPessoas):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= numeroPessoas
            return "Saindo..."

        else:
            return "Não tem ninguem aqui dentro do elevador"


#coloquei os valores padrão igual a zero porue faz sentido que o nosso elevador ja comece no primerio andar

e1 = Elevador(totalCapacidade=5,totalAndar=10)
print(f"Capacidade Total Pessoas: {e1.atualCapacidade}")
print(f"Andar Atual :{e1.atualAndar}")
print(e1.subir())
print(f"Andar Atual :{e1.atualAndar}")
print(f"Capacidade Total Pessoas: {e1.atualCapacidade}")
print(e1.sair(1))
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.subir())
print(e1.entrar(4))
print(e1.atualCapacidade)

print(e1.subir())
print(f"Andar Atual :{e1.atualAndar}")

