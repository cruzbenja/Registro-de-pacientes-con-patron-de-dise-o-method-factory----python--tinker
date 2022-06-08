class Moto:

    def __init__(self,nombre,x,y):
        self.nombre=nombre
        self.x=x
        self.y=y

    def encender(self):
        self.encendido=1
        

    def apagar(self):
        self.encendido=0

    def acelerar(self):
        if self.encendido == 1:
            self.x+=10


    
        