class Bateau:

    def __init__(self, couleur, type_energie):
        self.__type_energie = type_energie
        self._couleur = couleur
        
    @property
    def couleur(self):
        return self._couleur

    @property
    def type_energie(self):
        return self.__type_energie

    def avancer(self):
        print(self, "navigue")

    def tourner(self, direction):
        print(self, "vire à", direction)

    def accoster(self, port):
        print(self, "accoste au port", port)

    def arreter(self):
        print(self, "jete l'ancre")

    def __str__(self):
        return "Bateau {} à {}".format(self.couleur, self.type_energie)