from tkinter import *
from motocicleta import *

ventana=Tk()
moto1=Moto("pegasus 125",200,100)

ventana.geometry("800x600")
ventana.title("programa upds")
# estado inicial
def encender(self):
    moto1.encender()

def acelerar():
    moto1.acelerar()
    Boton1.place(x=moto1.x, y=moto1.y)

Boton1=Button(ventana,text=moto1.nombre,command=acelerar)
Boton1.place(x=moto1.x, y=moto1.y)
Boton0= Button(ventana, text="encender moto ", command=encender)
Boton0.place(x=10, y=10)
ventana.mainloop()