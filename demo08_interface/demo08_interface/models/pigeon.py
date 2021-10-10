from interfaces.i_oiseau import IOiseau


class Pigeon(IOiseau):

    def voler(self):
        print("Le pigeon vole")

    def manger(self, nourriture):
        print("Le pigeon picore", nourriture)


    def pondre(self):
        print("Le pigeon pond")

    def couver(self, item):
        print("Le pigeon couve", item)


if __name__ == '__main__':

    p = Pigeon()