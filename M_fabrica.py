class transporte:

    def __init__(self,transporte):
        self.transporte=transporte


    def entrega(self):
        print("entrega")   

class transportebarco(transporte):

    def __init__(self, marca):
        super(transportebarco, self).__init__(marca)
        print("has elegido hacer la entrega en barco",self.marca)

    def entrega(self):
        print("se ha hecho la entrega")

class transportecamion(transporte):

    def __init__(self, marca):
        super(transportecamion, self).__init__(marca)
        print("has elegido hacer la entrega en camion",self.marca)

    def entrega(self):
        print("se ha hecho la entrega")        
         
