"""
numeros = [1, 2, 3, 4]
dobro = [numero * 2 for numero in numeros]

for N in range(1, 5):
    multiplica = [numero * N for numero in numeros]

lenght = len(numeros)

print(numeros)
print(dobro)
print(multiplica)
print(lenght)
"""
numeros = (1, 2, 3, 4, 6, 7)


if len(numeros) == 5:
    print("aceptable")