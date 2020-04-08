"""
1 - calcular o primeiro digito verificador calculando os 9 numeros do cpf
490.605.938-47
    x
123 456 789
soma os resultados .sum

e divide a soma

2 - calcular o segundo digito usando os 9 numeros mais o primeiro digito verificador
490.605.938-47
012.345.678.9 / 11
3 - verificar se os dois numeros recebidos são iguais ao numero verificador

cpf = 490.605.938-47

"""
print("digite o cpf, sem . ou -")
cpf = tuple(input())
num1 = cpf[0]
num2 = cpf[1]
num3 = cpf[2]
num4 = cpf[3]
num5 = cpf[4]
num6 = cpf[5]
num7 = cpf[6]
num8 = cpf[7]
num9 = cpf[8]
num10 = cpf[9]
num11 = cpf[10]
num1a = int(num1) * 1
num2a = int(num2) * 2
num3a = int(num3) * 3
num4a = int(num4) * 4
num5a = int(num5) * 5
num6a = int(num6) * 6
num7a = int(num7) * 7
num8a = int(num8) * 8
num9a = int(num9) * 9
pridig = [num1a, num2a, num3a, num4a, num5a, num6a, num7a, num8a, num9a]
soma = sum(pridig)
print(soma)
verific_1 = soma % 11
num1a = 0
num2a = int(num2) * 1
num3a = int(num3) * 2
num4a = int(num4) * 3
num5a = int(num5) * 4
num6a = int(num6) * 5
num7a = int(num7) * 6
num8a = int(num8) * 7
num9a = int(num9) * 8
num10a = int(num10) * 9
pridig = [num1a, num2a, num3a, num4a, num5a, num6a, num7a, num8a, num9a, num10a]
soma = sum(pridig)
verific_2 = soma % 11
verificador_somado = (verific_1, verific_2)
verificador_original = (int(num10), int(num11))
if verificador_original == verificador_somado:
    print("O cpf é original")
else:
    print("o cpf não é original")