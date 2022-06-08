from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import filedialog
from PIL import ImageTk, Image

 

 
class Ventana(Tk):
    def __init__(self,dimension,titulo):
        super().__init__()
        self.geometry(dimension)
        self.title(titulo)
       
        self.formulario() 
         
        self.mainloop()
        
    def open():
        # Create a dialog box
        imagen=filedialog.askopenfilename(initialdir=" D:\ ", title="file uploader",
                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                             
        # # takes path that is selected by dialog box
        selected_image =Image.open(imagen)
        # # resize image
        selected_image = selected_image.resize((300, 205), Image.ANTIALIAS)
        # # displays an image
        imagen1 = ImageTk.PhotoImage(selected_image)
        label=Label(self, image=self.imagen1)
        label.place(x=200,y=350)
         

    def cerrar(self):
        pass


    def formulario(self):
        etiqueta=Label(self,text="Ci:")
        etiqueta.place(x=20,y=50)

        entrada =Entry()
        entrada.place(x=100, y=50)
        
        etiqueta1=Label(self,text="Nombre:")
        etiqueta1.place(x=20,y=100)

        entrada1 =Entry()
        entrada1.place(x=100, y=100)

        etiqueta2=Label(self,text="Apellidos:")
        etiqueta2.place(x=20,y=150)

        entrada2 =Entry()
        entrada2.place(x=100, y=150)

        etiqueta3=Label(self,text="Sexo:")
        etiqueta3.place(x=20,y=200)

        combo=ttk.Combobox(self,state="readonly",values=["masculino","femenino"])
        combo.place(x=100,y=200)

        etiqueta4=Label(self,text="Fecha Nac,:")
        etiqueta4.place(x=20,y=250)
        cal=DateEntry(width=20)
        cal.place(x=100,y=250)

        etiqueta5=Label(self,text="Profesion:")
        etiqueta5.place(x=20,y=300)

        combo1=ttk.Combobox(self,state="readonly",values=["Ing. De Sistemas","Ing.Informatica","Ing. Redes y Tele."])
        combo1.place(x=100,y=300)

        etiqueta6=Label(self,text="Especialidad:")
        etiqueta6.place(x=20,y=350)

        combo2=ttk.Combobox(self,state="readonly",values=["Bases de Datos","Ingeniería de Software","Sistemas de Información"])
        combo2.place(x=100,y=350)

        etiqueta7=Label(self,text="Titulo o Tipo:")
        etiqueta7.place(x=20,y=400)
        
        entrada3 =Entry()
        entrada3.place(x=100, y=400)

        etiqueta7=Label(self,text=" Telefono :")
        etiqueta7.place(x=300,y=50)

        entrada4 =Entry()
        entrada4.place(x=400, y=50)

        etiqueta7=Label(self,text=" email :")
        etiqueta7.place(x=300,y=100)

        entrada5 =Entry()
        entrada5.place(x=400, y=100)

        etiqueta8=Label(self,text=" Usuario :")
        etiqueta8.place(x=300,y=150)

        entrada5 =Entry()
        entrada5.place(x=400, y=150)

        etiqueta8=Label(self,text=" Contraseña :")
        etiqueta8.place(x=300,y=200)

        btn=Button(self,text='upload image',command=open)
        btn.place(x=400, y=150)
       



 
        
ventana1=Ventana("600x600","ventana nueva")

      
        
   
 


 

    
        

 