from persona import *
from abc import ABC, abstractmethod

class FabricarFormulario(ABC):
    def getForm(self, ventana, num):
        if (num == 1):
            return Asegurado(ventana)
        elif (num == 2):
            return NoAsegurado(ventana)
    