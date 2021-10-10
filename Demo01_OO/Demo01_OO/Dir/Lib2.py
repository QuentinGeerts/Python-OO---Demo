def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2


# print(__name__)
if __name__ == "__main__":
    nb1 = 40
    nb2 = 2
    res = addition(nb1, nb2)

    print(nb1, "+", nb2, "=", res)