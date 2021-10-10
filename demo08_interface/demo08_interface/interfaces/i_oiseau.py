# Rappel, les inferfaces n'existent pas en python !!!
from abc import ABC, abstractmethod


class IOiseau(ABC):

    @abstractmethod
    def voler(self):
        pass

    @abstractmethod
    def manger(self, nourriture):
        pass

    @abstractmethod
    def pondre(self):
        pass

    @abstractmethod
    def couver(self, item):
        pass