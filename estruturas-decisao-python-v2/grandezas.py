print("""
******************************
CÁLCULO DE GRANDEZAS ELÉTRICAS
******************************
1. Tensão
2. Resistência
3. Corrente
4. Sair
******************************
""")

op = int(input("Escolha uma opção: "))

if op == 1:
    r = float(input("Resistência: "))
    i = float(input("Corrente: "))
    print(f"Tensão: {r * i} V")

elif op == 2:
    u = float(input("Tensão: "))
    i = float(input("Corrente: "))
    print(f"Resistência: {u / i} Ohm")

elif op == 3:
    u = float(input("Tensão: "))
    r = float(input("Resistência: "))
    print(f"Corrente: {u / r} A")

elif op == 4:
    print("Encerrando...")

else:
    print("Opção inválida!")
