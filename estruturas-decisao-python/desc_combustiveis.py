tipo = input("A-Álcool G-Gasolina: ").upper()
litros = float(input("Litros: "))

if tipo == "A":
    preco = 2.89
    desc = 0.03 if litros <= 20 else 0.05

elif tipo == "G":
    preco = 4.95
    desc = 0.04 if litros <= 20 else 0.06

valor = litros * preco
final = valor - (valor * desc)

print(f"Total: R$ {final:.2f}")
