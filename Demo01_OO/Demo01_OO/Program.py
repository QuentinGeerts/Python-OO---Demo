from Lib import calcul_carre as cr

import Dir.Lib2 as M

# nb = 4
# res = cr(nb)
#
# print(res)
#
#
# val1 = 10
# val2 = 3
# res = M.soustraction(val1, val2)
#
# print(res)


# val = "42"
# test = isinstance(val, int)
#
# print(test)
#
#
# l = list("Toto")
# print(l)



from MyClass import MyClass

m = MyClass()

print(m.a)
print(m._a)
print(m._MyClass__a)

print(m.__dict__)

