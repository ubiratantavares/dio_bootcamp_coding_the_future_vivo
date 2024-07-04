from abc import ABC, abstractmethod

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass

    