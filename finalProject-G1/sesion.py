from factory import *
from registro import *
from tkinter import *
from tkinter import messagebox as ms
from hashlib import md5
import sqlite3


class login:
    def __init__(self):
    	# Window 
        self.root = Tk()
        self.root.title('CEDIMECC')
        self.root.geometry('430x300')
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.option = IntVar()
        #Create Widgets
        self.widgets()
        self.root.mainloop()

    #Login Function
    def login(self):
        if (self.username.get() == '' or self.password.get() == ''):
            ms.showerror('Error','Complete Los Campos !!!')
        #elif(self.password.get() == ''):
        #    ms.showerror('Error','Complete Los Campos !!!')
        elif(self.option.get() == 0):
            if (self.username.get() == 'admin' and self.password.get() == 'admin'):
                self.root.destroy()
                register()
            else:
                ms.showerror('Error','SELECCIONE TIPO DE FORMULARIO !!!')

        else:
            #Estableciendo Conexion
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()

            #Busqueda de Usuario
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            c.execute(find_user,[(self.username.get()),(md5(self.password.get().encode('utf-8')).hexdigest())])
            result = c.fetchall()
            if result:
                
                self.logf.pack_forget()
                self.root.destroy()
                
                ######## SI EL USUARIO EXISTE ENTRAMOS AL FORMULARIO INDICADO
                form = Tk()
                form.title('FORMULARIO DE REGISTRO CEDIMECC')
                form.geometry('700x650')
                Label(form, text="FORMULARIO DE REGISTRO", font="Helvetica 18 bold").place(x=200, y=10)
                FabricarFormulario().getForm(form, self.option.get()) #SELECCION 
                form.mainloop()
                ########
                            

            else:
                ms.showerror('Error','Usuario no encontrado.')
            
    def new_user(self):
    	#Estableciendo Conexion
        if (self.n_username.get() == ''):
            ms.showerror('Error','Complete Los Campos !!!')
        elif(self.n_password.get() == ''):
            ms.showerror('Error','Complete Los Campos !!!')
        else:
            with sqlite3.connect('quit.db') as db:
                c = db.cursor()

            #Verifica si User existe, sino lo registra

            find_user = ('SELECT username FROM user WHERE username = ?')
            c.execute(find_user,[(self.n_username.get())])        
            if c.fetchall():
                ms.showerror('Error',' Usuario Existente, Pruebe con uno diferente.')
            else:
                ms.showinfo('EXITO','Cuenta creada Exitosamente')
                self.log()
            #Crear una nueva cuenta 
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            c.execute(insert,[(self.n_username.get()),(md5(self.n_password.get().encode('utf-8')).hexdigest())])
            db.commit()        
    #def admin(self):
        
    # Métodos de embalaje del marco
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        if(self.username.get() == 'admin' and self.password.get() == 'admin'):
            self.logf.pack_forget()
            self.crf.pack()
        else:
            ms.showerror('Error','COLOQUE LOS DATOS DEL ADMIN PARA REGISTRAR !!!')        
        
    #Draw Widgets
    def widgets(self):
        
        self.logf = Frame(self.root,padx =10,pady = 20, bg='#0FE465')
        Label(self.logf,text = 'INICIO DE SESION', font = ('',20),pady=20,padx=5, bg='#0FE465').grid(row=0,column=0, columnspan=2)
        Label(self.logf,text = 'E-mail : ',font = ('',20),pady=5,padx=5, bg='#0FE465').grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.logf,text = 'Contraseña: ',font = ('',20),pady=5,padx=5, bg='#0FE465').grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=2,column=1)
        ############
        Radiobutton(self.logf, text = 'CON SEGURO', variable = self.option, value = 1, bg='#0FE465',pady=15).grid(row=3,column=0)
        Radiobutton(self.logf, text = 'SIN SEGURO', variable = self.option, value = 2, bg='#0FE465',pady=15).grid(row=3,column=1)
        ############
        Button(self.logf,text = ' Iniciar Sesión ',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.login).grid(row=4,column=0)
        Button(self.logf,text = ' Registrarse ',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.cr).grid(row=4,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.root,padx =10,pady = 20, bg='#0FC2E4')
        Label(self.crf,text = 'REGISTRO DE USUARIO', font = ('',20),pady=20,padx=5, bg='#0FC2E4').grid(row=0,column=0, columnspan=2)
        Label(self.crf,text = 'E-mail : ',font = ('',20),pady=5,padx=5, bg='#0FC2E4').grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.crf,text = 'Contraseña: ',font = ('',20),pady=5,padx=5, bg='#0FC2E4').grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=2,column=1)
        Label(self.crf,text = '', pady=15, bg='#0FC2E4').grid()
        Button(self.crf,text = 'Crear Usuario',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.new_user).grid(row=4,column=0)
        Button(self.crf,text = 'Iniciar Sesión',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.log).grid(row=4,column=1)


