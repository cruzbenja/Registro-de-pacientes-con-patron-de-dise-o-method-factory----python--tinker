#  clase salchicha
class sausage:
    def getNutrition(self):
        print("nutricion")


    def getColor(self):
        print("color")

    def getExpiration(self):
        print("Expiracion")


class gato:
    nombre=None

    def eat(self):
        s=sausage()
        s.getNutrition()

        # s.getNutrition()
        # print("comiendo")

      
rodolfo=gato()
rodolfo.eat()






