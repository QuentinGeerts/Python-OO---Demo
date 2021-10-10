class Math:

    __pi = 3.14159265359

    @staticmethod
    def get_pi():
        return Math.__pi

    @staticmethod
    def addition(nb1, nb2):
        return nb1 + nb2

    @staticmethod
    def puissance(nb1, exp):
        # return nb1 ** exp
        res = 1
        for i in range(exp):
            res *= nb1
        return res


if __name__ == '__main__':

    print(Math.get_pi())

    reponse = Math.addition(40, 2)
    print(reponse)

    carre = Math.puissance(2, 3)
    print(carre)


    carre = Math.puissance(2, 0)
    print(carre)