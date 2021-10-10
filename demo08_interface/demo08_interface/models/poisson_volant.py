from interfaces.i_oiseau import IOiseau
from interfaces.i_poisson import IPoisson


class PoissonVolant(IOiseau, IPoisson):

    def manger(self, nourriture):
        pass

    def voler(self):
        pass

    def pondre(self):
        pass

    def couver(self, item):
        pass

    def nager(self):
        pass



if __name__ == '__main__':
    valeur = PoissonVolant.__mro__
    print(valeur)

    c = PoissonVolant()

    c.__str__()
