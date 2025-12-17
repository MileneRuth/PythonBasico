


def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 451667353597
if e_par(numero):
    print(f"{numero}  é par.")
else:
    print(f"{numero} não é par")
    