"""
multiplique o valor de tempo por 60
"""


def mintosec(x):
    minuto = x * 60
    return minuto


print("diga me os minutos")
numero = int(input())

print(mintosec(numero))
