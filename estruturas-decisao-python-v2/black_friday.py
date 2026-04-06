valor = float(input("Valor da compra: R$ "))

print("1-Dinheiro  2-Débito  3-Crédito  4-PIX")
op = int(input("Forma de pagamento: "))

if op == 1:
    desc = 0.10
elif op == 2:
    desc = 0.05
elif op == 3:
    desc = 0.03
elif op == 4:
    desc = 0.075
else:
    desc = 0

final = valor - (valor * desc)
print(f"Valor final: R$ {final:.2f}")
