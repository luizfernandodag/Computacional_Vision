import random
# %%

class Usuario():
    def __init__(self,id,academia, tipo="normal"):
        self.tipo = tipo
        self.altere=-1
        self.id = id
        self.academia = academia
        
    def select_random_altere(self):
        
        if(self.academia.alteres_usados == self.academia.num_alteres ):
            raise Exception("Todos alteres usados")
        
        if(self.altere != -1):
            raise Exception("Já tem altere")
        
        altere = random.choice(self.academia.alteres)
        
        while(altere==-1):
            altere = random.choice(self.academia.alteres)
        
        self.academia.alteres[altere] = -1
        self.academia.alteres_usados+=1
        self.altere = altere
            
        return altere

            
        
        
    def pegar(self):
        altere = self.select_random_altere()
        return altere
    def devolver(self):
        if(self.academia.alteres_usados ==0):
            raise Exception("Sem alteres usados")
        if(self.altere==-1):
            raise Exception("Sem Altere Para Devolver")
        else:
            if(self.tipo=="normal" and self.academia.alteres[self.altere] == -1 ):
                self.academia.alteres[self.altere] = self.altere
                self.altere = -1
            elif(self.tipo!="normal"):
                if(self.academia.alteres[self.altere]==-1):
                    self.academia.alteres[self.altere] = self.altere
                else:
                    indexes = list(range(self.academia.num_alteres))
                    i = random.choice(indexes)
                    
                    while(self.academia.alteres[i] != -1 ):
                        i = random.choice(indexes)
                    self.academia.alteres[i] = self.altere
                    self.academia.alteres_usados-=1
                    self.altere = -1

                    
                        
                  
        
    def __str__(self):
        return f"Usuario(id={self.id}, tipo={self.tipo}, id = {self.id}, altere_usado={self.altere})"
 
    

class Academia():
    def __init__(self, num_users,num_alteres, percentagem_usuarios_errados=0.1):
        self.percetagem_usuarios_errado = percentagem_usuarios_errados
        self.num_users = num_users
        self.num_alteres = num_alteres
        self.usuarios = self.criarUsuarios(n=num_users)
        self.alteres = self.criar_alteres(num_alteres=num_alteres)
        self.alteres_usados = 0
        self.usuarios_usados = []
        
    def criar_alteres(self, num_alteres):
        alteres = list(range(num_alteres))
        for i in range(num_alteres):
            alteres[i]=i
        return alteres

        
    def print_users(self):
        for u in  self.usuarios:
            print(u)
    def print_alteres(self):
        for i,val in enumerate(self.alteres):
            print(f"{i}:{val}")
        
    
    def criarUsuarios(self, n):
        n_normais = int(n*(1-self.percetagem_usuarios_errado))
        print(f"n normais:{n_normais}")
        n_errados = n - n_normais
        
        usuarios = [Usuario(i,academia=self) for i in range(n_normais)]
        usuarios.extend([Usuario(i,academia=self,tipo= "errado") for i in range(n_normais, (n_normais+1 + n_errados))])
        return usuarios
    
    def select_user_not_used(self):
        
        if(len(self.usuarios_usados) == self.num_users):
            raise Exception("All users used")
        u = random.choice(self.usuarios)
        
        while(u in self.usuarios_usados):
            u = random.choice(self.usuarios)
              
        self.usuarios_usados.append(u)
        return u 
    
   
        
        
        
               
    def users_actions(self):
        for u in self.usuarios_usados:
            if(u.altere == -1):
                pass
                 
    def simular(self,n_passos):
        for _ in range(n_passos):
            u = self.select_user_not_used()
            u.pegar()
            
            
    
if __name__ == "__main__":
    academia = Academia(100,100)

    
    academia.print_alteres()
    academia.print_users()
# %%
