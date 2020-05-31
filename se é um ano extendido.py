
def ano_salto(ano):
    anos_salto = bool
    if int(ano) % 4 == 0:
        if int(ano) % 100 == 0:
            if int(ano) % 400 == 0:
                anos_salto = True
            else:
                anos_salto = False
    else:
        anos_salto = False
    return anos_salto


ano = input("de me o ano:")
print(ano_salto(ano))
