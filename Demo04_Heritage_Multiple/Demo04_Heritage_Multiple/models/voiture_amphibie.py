from models.bateau import Bateau
from models.voiture import Voiture


class VoitureAmphibie(Voiture, Bateau):

    def __init__(self, couleur, nb_roues, type_energie):
        # super().__init__("Rouge", nb_roues)
        Bateau.__init__(self, "Noir", type_energie)
        Voiture.__init__(self, "Rouge", nb_roues)
        self.__mode = 0  # 0 : sol / 1 : eau

    @property
    def mode_sol(self):
        return self.__mode == 0

    @property
    def mode_eau(self):
        return self.__mode == 1

    def changer_mode(self):
        self.__mode = (self.__mode + 1) % 2
        print("Changement de mode!")


    def avancer(self):
        if self.mode_sol:
            Voiture.avancer(self)
        else:
            Bateau.avancer(self)

    def arreter(self):
        if self.mode_sol :
            Voiture.arreter(self)
        else:
            Bateau.arreter(self)

    def accoster(self, port):
        if self.mode_eau:
            Bateau.accoster(self, port)
        else:
            print("Option non-valide")

    def tourner(self, direction):
        Voiture.tourner(self, direction)

    def __str__(self):
        return "Voiture Amphibie {}".format(self.couleur)



if __name__ == '__main__':
    va = VoitureAmphibie("Noir", 4, "Voile")

    print(VoitureAmphibie.__mro__)

    # print(va.couleur)
    # print(va.nb_roues)
    # print(va.type_energie)

    va.avancer()
    va.changer_mode()
    va.avancer()
    va.arreter()