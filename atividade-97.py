print("Programa para calcular o determinante de uma matriz")
print()

a = float(input("Informe o valor a: "))
b = float(input("Informe o valor b: "))
c = float(input("Informe o valor c: "))
d = float(input("Informe o valor d: "))

determinante = (a * d) - (b * c)

print(f"O determinante da matriz é: {determinante:.2f}")