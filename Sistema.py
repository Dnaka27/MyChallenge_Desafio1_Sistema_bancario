# operation

print(f"""
{'=' * 30}
{'Seja bem vindo'.center(30)}
{'-' * 30}""")

painel = """
Opções:

(1 / a). Depositar
(2 / b). Sacar 
(3 / c). Gerar extrato
(4 / d). Ver saldo
(5 / e). Encerrar sessao

------------------------------"""

saldo = 500
extrato = ""
qtd_saque = 0

while True:
    print(painel)
    opcao = str(input("Resposta: ")).upper()

    if opcao == "1" or opcao == "A":
        print(f"\n{'-|- Deposito -|-'.center(30)}")
        deposito = float(input("\nValor do deposito: "))
        if deposito > 0:
            saldo += deposito
            print("\n" + "- Deposito realizado -".center(30))
            extrato += f"Deposito de: {deposito}\n"
        else:
            print("! Valor invalido !" .center(30))

    if opcao == "2" or opcao == "B":
        print(f"\n{'-|- Saque -|-'.center(30)}")
        if qtd_saque < 3:
            if qtd_saque == 2:
                print("! Ultimo saque diario !".center(30))
            saque = float(input("\nValor do saque: "))
            if saque > 0 and saque <= 500 and saque < saldo:
                saldo -= saque
                print("\n" + "- Saque realizado -".center(30))
                extrato += f"Saque de: {saque}\n"
                qtd_saque += 1
            else:
                print("! Valor invalido !" .center(30))
        else:
            print("! Limite de saques excedido !".center(30))

    if opcao == "3" or opcao == "C":
        print(f"\n{'-|- Extrato -|-'.center(30)}")
        if extrato == "":
            print(f"\n{'(Extrato limpo/vazio)'.center(30)}")
        else:    
            print(f"\n{extrato}")
            print("-" * 30)

    if opcao == "4" or opcao == "D":
        print(f"\n{'-|- Saldo -|-'.center(30)}")
        print(f"\nSaldo: {saldo}")
        print("\n" + "-" * 30)

    if opcao == "5" or opcao == "E":
        print(f"\n{'Sessao encerrada'.center(30)}")
        print("=" * 30)
        break

