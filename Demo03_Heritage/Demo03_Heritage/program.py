from models.cadre import Cadre
from models.employe import Employe

c = Cadre("M", "H", 1)
e = Employe("Vanderquack", "Zaza", c)

c.realiser_planning()
e.realiser_encodage()