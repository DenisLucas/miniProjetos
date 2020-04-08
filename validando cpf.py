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
erro = True
E1 = True
E2 = True
E3 = True
while erro:
    print("digite o cpf, sem . ou -")
    cpf = tuple(input())
    erro1 = ("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")
    if cpf == erro1:
        space = None
    else:
        E1 = False
    if cpf[3] != '.':
        E2 = False
    if cpf[7] != '.':
        E3 = False
    if not E1 and not E2 and not E3:
        erro = False
    else:
        print("cpf invalido")
soma = 0
for I in range(0, 9):
    N = I + 1
    mult = int(cpf[I]) * N
    soma = soma + mult
    print(soma)

prim_verificador = soma % 11
sec_verificador = int(cpf[9])

mult = 0
soma = 0

if prim_verificador == sec_verificador:
    for I in range(0, 10):
        mult = int(cpf[I]) * I
        soma = soma + mult
        print(soma)

sec_verificador = soma % 11
orig_verificador = int(cpf[9]), int(cpf[10])
som_verificador = prim_verificador, sec_verificador

if orig_verificador == som_verificador:
    print("seu cpf é original")
else:
    print("seu cpf não é original")
