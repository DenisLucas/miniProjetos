22dasjdaspoerro = True
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
    if len(cpf) > 11:
        print("numeros em excesso (não se usa . ou - aqui)")
    else:
        E2 = False

    if len(cpf) < 11:
        print("numeros insuficientes")
    else:
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

prim_verificador = soma % 11
sec_verificador = int(cpf[9])

mult = 0
soma = 0

if prim_verificador == sec_verificador:
    for I in range(0, 10):
        mult = int(cpf[I]) * I
        soma = soma + mult

sec_verificador = soma % 11
orig_verificador = int(cpf[9]), int(cpf[10])
som_verificador = prim_verificador, sec_verificador

if orig_verificador == som_verificador:
    print("seu cpf é original")
else:
    print("seu cpf não é original")
