class Personne:

    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value


    def faire_pause(self):
        # Dans le print "self" fait appel a self.__str__()
        print("{0} est en pause".format(self))


    def __str__(self):
        return "{0} {1}".format(self.prenom, self.nom)


if __name__ == '__main__':
    p = Personne("Duck", "Riri")

    print(p)

    p.faire_pause()