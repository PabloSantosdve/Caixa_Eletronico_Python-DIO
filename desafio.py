menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("==== Bem-vindo à área de Depósito 💸 ====")
        deposito = float(input("Quanto você deseja depositar? "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"✅ Você depositou R${deposito:.2f}. Saldo atual: R${saldo:.2f}")
        else:
            print("❌ Valor inválido. Só é possível depositar valores positivos.")

    elif opcao == "s":
        print("=== Bem-vindo à área de Saque 💰 ===")

        if numero_saque >= LIMITE_SAQUE:
            print("❌ Limite diário de saques atingido.")
        else:
            valor_saque = float(input("Quanto você deseja sacar? "))

            if valor_saque <= 0:
                print("❌ Valor inválido. Só é possível sacar valores positivos.")
            elif valor_saque > saldo:
                print("❌ Saldo insuficiente.")
            elif valor_saque > limite:
                print(f"❌ O limite por saque é de R${limite:.2f}.")
            else:
                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque:.2f}\n"
                numero_saque += 1
                print(f"✅ Saque de R${valor_saque:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}")

    elif opcao == "e":
        print("===== EXTRATO 📋 =====")
        

    elif opcao == "q":
        print("Encerrando o sistema... 👋")
        break

    else:
        print("🚫 Operação inválida, por favor selecione novamente a operação desejada.")
