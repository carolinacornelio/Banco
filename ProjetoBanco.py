menu = """
[D] - Depositar
[S] - Sacar
[E] - Extrato
[U] - Criar usuário
[C] - Criar conta
[Q] - Sair
Digite a opção desejada:
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

def depositar(saldo,extrato,/):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:           
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido!")

def sacar(*,numero_saques=0, LIMITE_SAQUES=0, saldo=0, extrato="", limite=500, valor=0):
    if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
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
    
def exibir_extrato(saldo,/,*,extrato):
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Usuário já cadastrado!")
        
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Digite o endereço(logradouro, nro - bairro - cidade/sigla do estado): ")
    
    usuarios.append({"cpf":cpf,"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco})
    print("Usuário cadastrado com sucesso!")
    
def filtrar_usuario(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        nova_conta = {"AGENCIA": AGENCIA, "numero_conta": numero_conta, "saldo": 0, "limite": 500, "extrato": ""}
        contas.append(nova_conta)
        return nova_conta
    else:
        print("Usuário não encontrado!")
        return None

# def listar_contas(contas):
#     for conta in contas:
#         print(f"Agência: {conta['AGENCIA']}, Número da conta: {conta['numero_conta']}, Saldo: {conta['saldo']}, Limite: {conta['limite']}")
while True:
    opcao = input(menu)
    
    if opcao.upper() == "D":
        depositar(saldo,extrato)
        
    elif opcao.upper() == "S":
        sacar( numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, saldo=saldo, extrato=extrato, limite=limite, valor=0)
           
    elif opcao.upper() == "E":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao.upper() == "U":
        criar_usuario(usuarios)
        
    elif opcao.upper() == "C":
        num_conta = len(contas) + 1
        conta = criar_conta(AGENCIA,num_conta,usuarios)
        
        if conta:
            contas.append(conta)
        
    elif opcao.upper() == "Q":
        print("Saindo...")
        break

    # elif opcao.upper() == "L":
    #     listar_contas(contas)

    else:
        print("Opção inválida!")