import os

os.system('cls')
def print_jogo(m):
    print("      j=0   j=1   j=2 ")
    for i in range(3):
        print(f"i={i} |", end="")
        for j in range(3):
            print(f""+str(m[i][j]) + "    |", end="")
        print()

def criar_tabela():
    m = [[" " for _ in range(3)] for _ in range(3)]
    return m

m = criar_tabela()

print("Bem vindo ao jogo da velha")
print("--------------------------")


def verificar_fim(m):
    # verificar linhas
    for i in range(3):
        v = m[i][0]
        if(v == m[i][1] and v == m[i][2]):
            return v
        
        
            
    # verificar colunas
    for i in range(3):
        v = m[0][i]
        if(v == m[1][i] and v == m[2][i]):
            return v
    
    return False

def count_cells(m):
    count = 0
    for i in range(3):
        for j in range(3):
            if (m[i][j] != " "):
                count+=1
                  
    return count == 9
    
    
end = ""
rodada = 0

print("Jogador 0, escolha sua peça (X ou O (o maiusculo))")
j1 = input()
j2 = ""
if j1== "X":
    j2 = "O"
else:
    j2 = "X"
print(f"Jogador 0:{j1}, Jogador 1:{j2}")
        
simbolos = [j1,j2]        
while True:
    print_jogo(m)
    print(f"Jogador {(rodada)%2}, escolha a posicao i,j para seu símbolo. (digite i,j )")
    p = input().split(",")
    i,j = int(p[0]), int(p[1])
    while(m[i][j] != " "):
        print(f"Erro, posição ({i},{j}) já está ocupada com {m[i][j]} ")
        print(f"Jogador {(rodada)%2}, escolha a posicao i,j para seu símbolo. (digite i,j )")
        p = input().split(",")
        i,j = int(p[0]), int(p[1])
        
    
    
   
    s = simbolos[rodada%2]
    
    rodada+=1
    print_jogo(m)
   
    m[i][j] = s
    print_jogo(m)

    
    end = verificar_fim(m)
    if(end in ["O", "X"] or count_cells(m)  ):
        break
        
        

if end != False:
    print(f"{end} venceu!")
else:
    print("Empate!")
    
    
    
    
    
    
