print("Programa para somar duas matrizes")
print()

LINHAS = 4
COLUNAS = 3

def ler_matriz(nome):
    print(f"leitura  da {nome}")
    matriz = []
    for i in range(LINHAS):
        linha = []
        for j in range(COLUNAS):
            valor = float(input(f"Informe o valor para a posição [{i + 1}][{j + 1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

matriz_a = ler_matriz("Matriz A")
matriz_b = ler_matriz("Matriz B")

matriz_c = []
for i in range(LINHAS):
    linha_soma = []
    for j in range(COLUNAS):
        linha_soma.append(matriz_a[i][j] + matriz_b[i][j])
    matriz_c.append(linha_soma)

print("\n" + "="*35)
print(f"O resultado da soma é {matriz_c}")
print("="*35)
for linha in matriz_c:
    print("I".join(f"{val:8.2f}" for val in linha))
print("="*35)     
               
    