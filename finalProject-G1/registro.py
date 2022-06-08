from tkinter import *
from tkinter import ttk
import requests
from fpdf import FPDF
from tkinter import messagebox as ms
import sys

class register:
    def __init__(self):
        self.reg = Tk()
        self.reg.title('CEDIMECC')
        
        self.reg.geometry('1250x450')    
        self.wid()
        self.reg.mainloop()
    
    def wid(self):
        Label(self.reg, text="ADMINISTRADOR DE REGISTROS", font="FiraCode 18 bold").place(x=180, y=20)
        Label(self.reg, text=" CEDIMECC ", font="FiraCode 18 bold").place(x=300, y=50)

        self.tabla=ttk.Treeview(self.reg)
        self.tabla.place(x=30,y=100)
        self.desplazate=ttk.Scrollbar(self.reg, orient="vertical", command=self.tabla.yview)
        self.desplazate.place(x=30,y=100,height=230)
        self.tabla.configure(yscrollcommand=self.desplazate.set)
        self.tabla['columns']=('id', 'ci', 'nombres', 'paterno','materno', 'sexo', 'fecha_nacimiento', 'biografia', 'foto', 'nacionalidad', 'residencia', 'ocupacion', 'especialidad', 'titulo', 'numero_seguro')
        self.tabla.column("#0", width=0)
        self.tabla.column("id", width=50)
        self.tabla.column("ci", width=80)
        self.tabla.column("nombres", width=80)
        self.tabla.column("paterno", width=80)
        self.tabla.column("materno", width=80)
        self.tabla.column("sexo", width=80)
        self.tabla.column("fecha_nacimiento", width=80)
        self.tabla.column("biografia", width=80)
        self.tabla.column("foto", width=80)
        self.tabla.column("nacionalidad", width=80)
        self.tabla.column("residencia", width=80)
        self.tabla.column("ocupacion", width=80)
        self.tabla.column("especialidad", width=80)
        self.tabla.column("titulo", width=80)
        self.tabla.column("numero_seguro", width=80)

        self.tabla.heading("#0",text="")
        self.tabla.heading("id",text="id")
        self.tabla.heading("ci",text="ci")
        self.tabla.heading("nombres",text="nombres")
        self.tabla.heading("paterno",text="paterno")
        self.tabla.heading("materno",text="materno")
        self.tabla.heading("sexo",text="sexo")
        self.tabla.heading("fecha_nacimiento",text="fecha_nacimiento")
        self.tabla.heading("biografia",text="biografia")
        self.tabla.heading("foto",text="foto")
        self.tabla.heading("nacionalidad",text="nacionalidad")
        self.tabla.heading("residencia",text="Genresidenciaero")
        self.tabla.heading("ocupacion",text="ocupacion")
        self.tabla.heading("especialidad",text="especialidad")
        self.tabla.heading("titulo",text="titulo")
        self.tabla.heading("numero_seguro",text="numero_seguro")
       
        btn_mostrar = Button(text="MOSTRAR", font="Helvetica 14 bold",   command=lambda:[self.mostrar()]).place(x=400, y=370)
        btn_eliminar = Button(text="ELIMINAR", font="Helvetica 14 bold", command=lambda:[self.eliminar(), self.mostrar()]).place(x=520, y=370)
        btn_imprimir = Button(text="IMPRIMIR", font="Helvetica 14 bold", command=lambda:[self.imprimir()]).place(x=635, y=370)
        
   
    def mostrar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        canciones=requests.get('http://tecnoprofe.com/api/paciente')
        print(canciones.json())
        for dato in canciones.json():
            self.tabla.insert(parent='', index='end', 
            values=(dato['id'],dato['ci'], dato['nombres'], dato['paterno'], dato['materno'], dato['sexo'], dato['fecha_nacimiento'], dato['biografia'], dato['foto'], dato['nacionalidad'], dato['residencia'], dato['ocupacion'], dato['especialidad'], dato['titulo'], dato['numero_seguro']))
    
    def eliminar(self):
        marcado= self.tabla.focus()
        actual=self.tabla.item(marcado)['values'][0]
        dato=actual
        requests.delete('http://tecnoprofe.com/api/paciente/'+ str(dato))
  
   #IMRPIMIRREPORTE
    def imprimir(self):
        pdf =FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=10)
        stoutOrigin = sys.stdout
        sys.stdout=open("reportes/ReportTXT.txt", "w")
        canciones=requests.get('http://tecnoprofe.com/api/paciente')
        for fila in canciones.json():
            print(" [",fila['id'],"- ] [",fila['ci']," ] [",fila['nombres']," ] [",fila['paterno']," ] [ ",fila['materno']," ] [",fila['sexo']," ] [",fila['fecha_nacimiento']," ]\n [",fila['biografia']," ]\n [",fila['foto']," ]\n [",fila['nacionalidad']," ] [",fila['residencia']," ] [",fila['ocupacion']," ] [",fila['especialidad']," ]\n [",fila['titulo']," ] [",fila['numero_seguro']," ]\n --------------------------------------------------------------------------------------------------------- ")
        sys.stdout=open("reportes/ReportTXT.txt", "r")
        for x in sys.stdout:         

          pdf.cell(w=200,h=15,txt = x,ln = 1,align = 'C')
          
        pdf.output('reportes/ReportPDF.pdf')

        ms.showinfo('EXITO','REGISTROS GUARDADOS EN PDF & TXT')

