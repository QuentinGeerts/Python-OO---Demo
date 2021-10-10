from models.personne import Personne


class Cadre(Personne):

    def __init__(self, nom, prenom, prime):
        super().__init__(nom, prenom)
        self.__prime = prime


    @property
    def prime(self):
        return self.__prime

    @prime.setter
    def prime(self, value):
        self.__prime = value


    def realiser_planning(self):
        print("{0} réalise le planning".format(self))


    def __str__(self):

        text = super().__str__() + " (Cadre)"
        return text



if __name__ == '__main__':
    c = Cadre("Picsou", "Balthazar", 5000)

    c.faire_pause()
    c.realiser_planning()