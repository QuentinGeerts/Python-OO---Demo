class Voiture:

    def __init__(self, couleur, nb_roues):
        self._couleur = couleur
        self.__nb_roues = nb_roues

    @property
    def couleur(self):
        return self._couleur

    @property
    def nb_roues(self):
        return self.__nb_roues

    def avancer(self):
        print(self, "roule")

    def tourner(self, direction):
        print(self, "tourne à", direction)

    def arreter(self):
        print(self, "s'arrete")

    def __str__(self):
        return "Voiture " + str(self.couleur)


