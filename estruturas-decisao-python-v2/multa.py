velocidade = float(input("Digite a velocidade do carro (Km/h): "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 50
    print(f"\nVocê ultrapassou o limite!")
    print(f"Excedeu: {excesso:.0f} Km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("\nVelocidade dentro do limite.")
