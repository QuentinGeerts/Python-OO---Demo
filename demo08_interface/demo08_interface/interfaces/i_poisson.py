from abc import abstractmethod, ABC

class IPoisson(ABC):

    @abstractmethod
    def nager(self):
        pass

    @abstractmethod
    def manger(self):
        pass