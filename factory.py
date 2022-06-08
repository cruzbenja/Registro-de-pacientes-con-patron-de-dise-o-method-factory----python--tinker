
from M_fabrica import transportebarco, transportecamion
class factorytransporte:
    @staticmethod
    def get_transporte(tipo, marca):

        if tipo =="barco":
            
            return transportebarco(marca)
        elif tipo == "camion":
            return transportecamion(marca)

        else:
            return "tipo invalido"    
