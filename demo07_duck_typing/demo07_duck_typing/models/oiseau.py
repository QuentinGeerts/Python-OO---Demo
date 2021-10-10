# un oiseau connait la méthode "vole"


class Pigeon():

    def vole(self):
        print("Le pigeon vole")


class Chien():

    def marche(self):
        print("Le chien marche")


class Avion():

    def vole(self):
        print("L'oiseau vole")


if __name__ == '__main__':

    def est_oiseau(obj) :
        return "vole" in dir(obj)

    p = Pigeon()

    c = Chien()

    if est_oiseau(p):
        p.vole()

    if est_oiseau(c):
        c.vole()




