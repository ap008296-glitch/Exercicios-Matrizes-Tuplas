print("Programa para fazer uma tupla com nome e idade de 10 pessoas")
print()

pessoas = []
for i in range(10):
    nome = input(f"Informe o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Informe a idade de {nome}: "))
    pessoa = (nome, idade)
    pessoas.append(pessoa)

print("\n" + "="*40)
print("Grupo 1: Menores de 18 anos")
print("="*40)
menores = [p for p in pessoas if p[1] < 18]
if menores:
    for nome, idade in menores:
        print(f". Nome: {nome:<20} idade: {idade} anos")
else:
    print("Nenhuma pessoa cadastrada neste grupo")

print("\n" + "="*40)
print("Grupo 2: 18 anos ou mais")
print("="*40)
maiores = [p for p in pessoas if p[1] >= 18]
if menores:
    for nome, idade in maiores:
        print(f". Nome: {nome:<20} idade: {idade} anos")
else:
    print("Nenhuma pessoa cadastrada neste grupo")                        