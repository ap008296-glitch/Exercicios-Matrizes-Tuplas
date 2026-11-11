def calcular_determinante():
    print("Informe os valores da matriz: ")
    a = float(input("Valor a (linha 1, coluna 1): "))
    b = float(input("Valor b (linha 1, coluna 2): "))
    c = float(input("Valor c (linha 1, coluna 3): "))

    d = float(input("Valor d (linha 2, coluna 1): "))
    e = float(input("Valor e (linha 2, coluna 2): "))
    f = float(input("Valor f (linha 2, coluna 3): "))

    g = float(input("Valor g (linha 3, coluna 1): "))
    h = float(input("Valor h (linha 3, coluna 2): "))
    i = float(input("Valor i (linha 3, coluna 3): "))

    det_M = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d *i) - (a * f * h)

    print(f"O determinante da matriz é: {det_M:.2f}")

calcular_determinante()   