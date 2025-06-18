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

    opcao = input(menu)

    if opcao == "d" or "D":
        print("Deposito")
    elif opcao == "s" or "S":
        print("Saque")
    elif opcao == "e" or "E":
        print("Extrato")
    elif opcao == "q" or "Q":
        print("Encerrando o sistema...")
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")