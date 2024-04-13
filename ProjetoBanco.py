menu = """
[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair
Digite a opção desejada:
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.upper() == "D":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:           
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")
        
    elif opcao.upper() == "S":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
            continue
        else:
            valor = float(input("Digite o valor do saque: "))
            if valor > 0 and valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                else:
                    print("Saldo insuficiente!")
            else:
                print("Valor inválido!")
           
    elif opcao.upper() == "E":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao.upper() == "Q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")