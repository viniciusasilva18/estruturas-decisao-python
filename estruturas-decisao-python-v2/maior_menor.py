n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
soma = n1 + n2 + n3
media = soma / 3

print("\nResultados:")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print(f"Média: {media}")
