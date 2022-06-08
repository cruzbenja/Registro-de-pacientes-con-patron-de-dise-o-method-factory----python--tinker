from registro import register
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image
from tkinter import messagebox as ms
import requests
from tkinter import filedialog


class Persona():

    def __init__(self, ventana):
        #METODO PARA CARGAR LA IMAGEN
        self.ventana = ventana
        def cargarImg():  
            global img, ruta
            #global ruta
            ventana.filename = filedialog.askopenfilename(filetypes = [("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")], title="SELECCIONE UNA FOTO", initialdir="/src")
            ruta = ventana.filename
            img = ImageTk.PhotoImage(Image.open(ventana.filename).resize((150, 150), Image.ANTIALIAS))
            Label(image=img).place(x=440, y=200)

            
        lbl_name = Label(ventana, text="Nombres : ").place(x=50, y=50)
        self.name = Entry(ventana)
        self.name.place(x=200, y=50)    
    

        lbl_apellido = Label(ventana, text="Ap. Paterno : ").place(x=50, y=80)
        self.apellido1 = Entry(ventana)
        self.apellido1.place(x=200, y=80)

        lbl_apellido = Label(ventana, text="Ap. Materno : ").place(x=50, y=110)
        self.apellido2 = Entry(ventana)
        self.apellido2.place(x=200, y=110)
    

        lbl_sexo = Label(ventana, text="Sexo : ").place(x=50, y=140)
        self.sexo = ttk.Combobox(ventana,
            textvariable=StringVar(), 
            state='readonly', 
            values=['Masculino', 'Femenino']
            )
        self.sexo.place(x=200, y=140)


        lbl_fecha = Label(ventana, text="Fecha Nacimiento :").place(x=50, y=170)
        self.fecha = DateEntry(ventana,width=20)
        self.fecha.place(x=200, y=170)


        lbl_history = Label(ventana, text="Biografia : ").place(x=50, y=380)
        self.biografia = Text(ventana, width=72, height=10)
        self.biografia.place(x=50, y=410)


        lbl_telefono = Label(ventana, text="Telefono : ").place(x=400, y=50)
        self.telefono = Entry(ventana,textvariable=IntVar())
        self.telefono.place(x=500, y=50)


        lbl_cedula = Label(ventana, text="C.I. : ").place(x=400, y=80)
        self.cedula = Entry(ventana)
        self.cedula.place(x=500, y=80)


        lbl_residencia = Label(ventana, text="Residencia : ").place(x=400, y=110)
        self.residencia = Entry(ventana)
        self.residencia.place(x=500, y=110)


        lbl_nacionalidad = Label(ventana, text="Nacionalidad : ").place(x=400, y=140)
        self.nacionalidad = Entry(ventana)
        self.nacionalidad.place(x=500, y=140)
    
    
        btn_img = Button(ventana, text="CARGAR IMAGEN", width=30, command=cargarImg).place(x=405, y=170)
        

        #BOTONES DE GUARDAR Y SALIR
        btn_save = Button(ventana,text="GUARDAR", font="Helvetica 10 bold", command=self.mandar).place(x=250, y=600)
        btn_quit = Button(ventana,text="CERRAR", command=lambda:[quit()], font="Helvetica 10 bold").place(x=350, y=600)

    #METODO PARA CONECTAR A LA API CON EL BOTON GUARDAR
    

    def mandar(self):
        requests.post("http://tecnoprofe.com/api/paciente", data = {
            'ci':self.cedula.get(),
            'nombres':self.name.get(),
            'paterno':self.apellido1.get(),
            'materno':self.apellido2.get(),
            'sexo':self.sexo.get(),
            'fecha_nacimiento':self.fecha.get(),
            'biografia':self.biografia.get("1.0","end-1c"),
            'foto':ruta,
            'nacionalidad':self.nacionalidad.get(),
            'residencia':self.residencia.get(),
            'ocupacion':txt_ocupacion.get(),
            'especialidad':txt_especialidad.get(),
            'titulo':txt_titulo.get(),
            'numero_seguro': txt_numseg.get()
            })
        ms.showinfo('EXITO','REGISTROS GUARDADOS CORRECTAMENTE')
        
    def cambiar(self):
        self.ventana.destroy()
        register()
    
           

class Asegurado(Persona):
    def __init__(self, ventana):
        super().__init__(ventana)
      
        
        global txt_ocupacion, txt_especialidad, txt_titulo, txt_numseg

        dibujar = Canvas(ventana, width= 300, height=170)
        dibujar.place(x=45, y=202)
        dibujar.create_rectangle(5,5,300,170)

        Label(ventana, text="PERSONA ASEGURADA", font="Helvetica 10 bold").place(x=110, y=210)
        Label(ventana, text="Ocupación : ").place(x=60, y=240)
        txt_ocupacion = Entry(ventana)
        txt_ocupacion.place(x=210, y=240)


        Label(ventana, text="Especialidad : ").place(x=60, y=270)
        txt_especialidad = Entry()
        txt_especialidad.place(x=210, y=270)


        Label(ventana, text="Titulo : ").place(x=60, y=300)
        txt_titulo = Entry(ventana)
        txt_titulo.place(x=210, y=300)

        Label(ventana, text="Num. Seguro : ").place(x=60, y=330)
        txt_numseg = Entry(ventana, textvariable=IntVar())
        txt_numseg.place(x=210, y=330)

        

class NoAsegurado(Persona):
    def __init__(self, ventana):
        super().__init__(ventana)
        global txt_sus
        dibujar = Canvas(ventana, width= 300, height=170)
        dibujar.place(x=45, y=202)
        dibujar.create_rectangle(5,5,300,170)

        Label(ventana, text="PERSONA NO ASEGURADA", font="Helvetica 10 bold").place(x=120, y=210)
        Label(ventana, text="Area Laboral :").place(x=60, y=240)
        txt_soat = Entry(ventana).place(x=210, y=240)


        Label(ventana, text="Codigo SUS :").place(x=60, y=270)
        txt_sus = Entry(ventana)
        txt_sus.place(x=210, y=270)


        lbl_laburo = Label(ventana, text="Posicion Laboral : ").place(x=60, y=300)
        txt_laburo = Entry(ventana).place(x=210, y=300)

        lbl_emp = Label(ventana, text="Empresa : ").place(x=60, y=330)
        txt_emp = Entry(ventana).place(x=210, y=330)


