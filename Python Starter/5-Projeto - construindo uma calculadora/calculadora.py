ops = {
    0:"Soma",
    1:"Subtração",
    2:"Multiplicação",
    3:"Divisão",
    4:"Exponenciação",
    }

def print_ops():
    for op in ops:
        print(str(op) + ":  "+ops[op])
        
def get_num():
    print("Digite um número")
    return float(input())
def calc_opcao(opcao):
    match opcao:
        case 0:
            
            n1 = get_num()
            n2 = get_num()
            s = n1+n2 
            print(f"\n{n1} + {n2}={s}\n")
            print("Deseja fazer outro cálculo? 0-SIM, 1-NÃO")
            continuar = int(input())
            return continuar
        case 1:
            
            n1 = get_num()
            n2 = get_num()
            s = n1-n2 
            print(f"\n{n1} - {n2}={s}\n")
            print("Deseja fazer outro cálculo? 0-SIM, 1-NÃO")
            continuar = int(input())
            return continuar
        case 2:
            
            n1 = get_num()
            n2 = get_num()
            s = n1*n2 
            print(f"\n{n1} * {n2}={s}\n")
            print("Deseja fazer outro cálculo? 0-SIM, 1-NÃO")
            continuar = int(input())
            return continuar
        case 3:
            
            n1 = get_num()
            n2 = get_num()
            s = n1/n2 
            print(f"\n{n1} / {n2}={s}\n")
            print("Deseja fazer outro cálculo? 0-SIM, 1-NÃO")
            continuar = int(input())
            return continuar
        case 4:
            
            n1 = get_num()
            n2 = get_num()
            s = n1**n2 
            print(f"\n{n1}**{n2}={s}\n")
            print("Deseja fazer outro cálculo? 0-SIM, 1-NÃO")
            continuar = int(input())
            return continuar
            
            
        case _:
            print("Opção não disponível")
            return 0
        
while True:
    print_ops()
    print("\nEscolha a operação desejada:")
    opcao = int(input())
    continuar = calc_opcao(opcao)
    if continuar == 1:
        break
    
