print("Programa para diferenciar uma matriz identidade")
print()

TAMANHO = 3
matriz = []
for i in range(TAMANHO):
    linha = []
    for j in range(TAMANHO):
        valor = float(input(f"Informe o valor para [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha) 
    eh_identidade = True

    for i in range(TAMANHO):
        for j in range(TAMANHO):
            if i == j:
                if matriz[i][j] != 1:
                    eh_identidade = False
                    break
            else:
                if matriz[i][j] != 0:
                     eh_identidade = False
                     break
        if not eh_identidade:
            break
print("Matriz informada: ")
for linha in matriz:
    print(" ".join(f"{val:g}" for val in linha))
if eh_identidade:
    print("Resultado: A matriz informada é uma matriz identidade!")
else:
    print("Resultado: A matriz informada NÃO é uma matriz identidade")                            
