import os
import random

s_hello = "Bem vindo ao jogo de Papel, Pedra ou Tesoura"

pontos_eu = 0
pontos_computador = 0
opcoes = ["Papel","Pedra","Tesoura"] 

def print_placar():
    global pontos_eu, pontos_computador
    print("PLACAR:")
    print(f"Você:{pontos_eu}")
    print(f"Computador:{pontos_computador}\n\n")

def print_opcoes():
    print("Escolha seu lance:")    
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")
    
def avaliar_rodada(minha_escolha:str, computador_escolha:str):
    
    if minha_escolha == computador_escolha:
        print("Empate")
        return [0,0]
    elif minha_escolha == "Papel":
            if computador_escolha == "Pedra":
                print("Você venceu!")
                return [1,0]
            elif computador_escolha == "Tesoura":
                print("Computador Venceu")
                return [0,1]
    elif minha_escolha == "Pedra":
        if computador_escolha == "Tesoura":
            print("Você venceu!")
            return [1,0]
        elif computador_escolha == "Papel":
            print("Computador Venceu")
            return [0,1]
    elif minha_escolha == "Tesoura":
        if computador_escolha == "Papel":
            print("Você venceu!")
            return [1,0]       
        elif computador_escolha == "Pedra":
                print("Computador Venceu")
                return [0,1]
    
    
    return [0,0]
    
    
def rodada(minha_escolha:str, computador_escolha:str):
    global pontos_eu, pontos_computador
    print("================")
    print(f"Sua jogada: {minha_escolha}")    
    print(f"Jogada do computador: {computador_escolha}")
    p = avaliar_rodada(minha_escolha, computador_escolha)
    pontos_eu += p[0]
    pontos_computador += p[1]
    
        
            
                

def jogar():
   
    global opcoes
    while True:
        os.system('cls')
        print_placar()
        print_opcoes()
        try: 
            escolha = int(input())
            minha_escolha = opcoes[escolha]
            c_escolha = random.choice(opcoes)
            print(minha_escolha)
            print(c_escolha)
            rodada(minha_escolha, c_escolha)
            print("================")
            print("\nJogar Novamente: 0 - SIM | 1 - NÃO ")
            b = int(input())
            if (b == 1):
                break
        
            
        
        except Exception as e:
            print(f"Error:{e}")
            
    os.system('cls')        
    if(pontos_eu> pontos_computador):
        print("RESULTADO FINAL: Você venceu")
    elif(pontos_eu< pontos_computador):
        print("RESULTADO FINAL: Computador venceu")
    else:
        print("RESULTADO FINAL: Empate")
        
    
    
    
if __name__ == "__main__":
    jogar()
