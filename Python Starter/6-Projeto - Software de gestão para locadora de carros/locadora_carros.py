import os

os.system('cls')

print("============")
print("Bem vindo à locadora de carros!")
print("============")

ops = ["Mostrar portifólio", "Alugar um carro", "Devolver um carro"]

portifolio = {"Crevrolet Tracker":120, "Crevrolet Onix":90,"Crevrolet Spin":150,"Hyundai HB20":85,"Hyundai Tucson":120,"Fiat Uno":60,"Fiat Mobi":70,"Fiat Pulse":130 }
alugueis = []



def print_ops():
    global ops 
    for i, s in enumerate(ops):
        print(str(i)+" - "+ s, end=" | ")
        

def print_alugueis():
    print(alugueis)
def print_portifolio():
    global portifolio
    
    i = 0
    for car, valor in portifolio.items():
        print(f"[{i}] {car} - R$ {valor}/dia")
        i+=1
        
def alugar():
    global portifolio
    global alugueis
    print("[ ALUGAR ] Dê uma olhada em nosso portifólio.")
    print_portifolio()
    carros = list(portifolio.items())
    print("=======")
    print("Escolha o código do carro")
    cod = int(input())
    
    print("Escolha por quantos dias deseja alugar:")
    dias = int(input())
    total = dias * carros[cod][1]
    print(f"Você escolheu {carros[cod][0]} por {dias} dias.\nO aluguel totalizaria R$ {total}. Deseja Alugar?\n\n 0-SIM | 1-NÃO")
    sim = int(input())
    if sim == 0:
        car = carros[cod]
        alugueis.append(car)
        del portifolio[car[0]]
        return [car, dias]
    else:
        return -1
    
def devolver():
    global alugueis
    global portifolio
    print("Segue a lista de carros alugados")
    i = 0
    for car in alugueis:
        print(f"[{i}] {car[0]} - R$ {car[1]}/dia")
        i+=1
        
    print("Escolha o código do carro que deseja devolver:")
    i = int(input())
    
    car = alugueis[i]
    portifolio[car[0]] = car[1]
    print(f"Obrigado por devolver o carro {car[0]}")
    print("==========")
    print("0-CONTINUAR| 1 - SAIR")
    op = int(input())
    if op == 1:
        return -1
    else:
        return 0
    
    #portifolio = {"Crevrolet Tracker":120,    
    
while True:
    # get op
    
    print_ops()
    print("\nO que deseja fazer?")
    op = int(input())

    if op==0:
        print_portifolio()
        
    elif op == 1:
        car = alugar()
        if car != -1:
            print(f"Parabéns você alugou o {car[0][0]} por {car[1]} dias")
            
          
            print("============")
            
            print("0 - CONTINUAR | 1 SAIR")
            continuar = int(input())
            if continuar == 1:
                break;

        
        
    elif op == 2:
        op = devolver()
        if op == -1:
            break
             
    