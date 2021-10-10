from models.personne import Personne


class Employe(Personne):

    def __init__(self, nom, prenom, cadre):
        super().__init__(nom, prenom)
        self.__sup = cadre

    @property
    def sup(self):
        return self.__sup

    def realiser_encodage(self):
        print("{} realise un encodage".format(self))

    def reunion_sup(self):
        print("{} est en réunion avec {}".format(self, self.sup))


    def __str__(self):

        return super().__str__() + " (Employé)"


if __name__ == '__main__':

    from models.cadre import Cadre

    c = Cadre("M", "H", 1)
    e = Employe("Vanderquack", "Zaza", c)

    c.realiser_planning()
    e.realiser_encodage()

    c.faire_pause()
    e.faire_pause()

    e.reunion_sup()