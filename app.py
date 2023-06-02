from tkinter import Tk, Frame, Label, Text, Radiobutton, IntVar, Button, StringVar
from database import Db

class App:
    
    def __init__(self):
        
        # Ventana padre
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('Consultas bases de datos')
        
        # Ventana principal
        self.v_principal = Frame(self.root)
        self.v_principal.grid(row= 0, column= 4, padx= 25)
        
        # Widgets
        self.r_1 = Label(self.v_principal)
        self.r_1.config(text='ENUNCIADO DE EJERCICIO', font='arial 14 bold')
        self.r_1.grid(row= 1, column= 1, columnspan= 3, pady= 10)
        
        self.salida = Text(self.v_principal)
        self.salida.config(padx= 20, pady= 10, height= 10)
        self.salida.grid(row= 2, column= 1, columnspan= 3)
        
        self.r_2 = Label(self.v_principal)
        self.r_2.grid(row= 3, column= 4)
        
        self.opcion_1 = IntVar()
        self.opcion_1.set(1)
        
        self.bd_nba = Radiobutton(self.v_principal)
        self.bd_nba.config(text='NBA', font='arial 14 bold', pady=15, value= 1, variable= self.opcion_1)
        self.bd_nba.grid(row= 3, column= 0, columnspan= 2)
        
        self.bd_jardineria = Radiobutton(self.v_principal)
        self.bd_jardineria.config(text='JARDINERÍA', font='arial 14 bold', pady=15, value= 2, variable= self.opcion_1)
        self.bd_jardineria.grid(row= 3, column= 3, columnspan= 2)
        
        self.r_4 = Label(self.v_principal)
        self.r_4.config(pady= 25)
        self.r_4.grid(row= 4, column= 4)
        
        self.opcion_2 = IntVar()
        self.opcion_2.set(1)
        
        self.query_tipo_s = Radiobutton(self.v_principal)
        self.query_tipo_s.config(text='SIMPLE', font='arial 14 bold', value= 1, variable= self.opcion_2)
        self.query_tipo_s.grid(row= 4, column= 1)
        
        self.query_tipo_sc = Radiobutton(self.v_principal)
        self.query_tipo_sc.config(text='SUBCONSULTA', font='arial 14 bold', value= 2, variable= self.opcion_2)
        self.query_tipo_sc.grid(row= 4, column= 2)
        
        self.query_tipo_c = Radiobutton(self.v_principal)
        self.query_tipo_c.config(text='COMPUESTA', font='arial 14 bold', value= 3, variable= self.opcion_2)
        self.query_tipo_c.grid(row= 4, column= 3)
        
        self.r_3 = Label(self.v_principal)
        self.r_3.config(pady= 20)
        self.r_3.grid(row= 5, column= 4)
        
        self.mostrar = Button(self.v_principal)
        self.mostrar.config(text= 'Mostrar', justify= 'center', command= self.enunciado)
        self.mostrar.grid(row= 5, column= 1, columnspan= 3)
        
        self.r_4 = Label(self.v_principal)
        self.r_4.config(pady= 20)
        self.r_4.grid(row= 6, column= 4)
        
        self.num_ejercicios = IntVar()
        self.num_ejercicios.set(0)
        
        self.r_5 = Label(self.v_principal)
        self.r_5.config(text= 'Nº de ejercicios: {}'.format(self.num_ejercicios.get()))
        self.r_5.grid(row= 6, column= 1)
        
        self.ejercicio = IntVar()
        self.ejercicio.set(0)
        
        self.r_6 = Label(self.v_principal)
        self.r_6.config(text= 'Ejercicio nº: {}'.format(self.ejercicio.get()))
        self.r_6.grid(row= 6, column= 3)
        
        self.r_7 = Label(self.v_principal)
        self.r_7.config(pady= 20)
        self.r_7.grid(row= 7, column= 4)
        
        self.b_atras = Button(self.v_principal)
        self.b_atras.config(text= 'Atras', width= 10, command= self.boton_atras)
        self.b_atras.grid(row= 7, column= 0, columnspan= 2)
        
        self.b_siguiente = Button(self.v_principal)
        self.b_siguiente.config(text= 'Siguiente', width= 10, command= self.boton_siguiente)
        self.b_siguiente.grid(row= 7, column= 3, columnspan= 2)
        
        self.r_8 = Label(self.v_principal)
        self.r_8.config(text='SOLUCIÓN DE EJERCICIO', font='arial 14 bold')
        self.r_8.grid(row= 8, column= 1, columnspan= 3, pady= 10)
        
        self.sld = StringVar()
        self.sld.set('')
        
        self.salida_s = Text(self.v_principal)
        self.salida_s.config(padx= 20, pady= 10, height= 10)
        self.salida_s.grid(row= 9, column= 1, columnspan= 3)
        
        self.r_9 = Label(self.v_principal)
        self.r_9.config(pady= 20)
        self.r_9.grid(row= 10, column= 4)
        
        self.mostrar_s = Button(self.v_principal)
        self.mostrar_s.config(text= 'Mostrar', justify= 'center', command= self.solucion)
        self.mostrar_s.grid(row= 10, column= 1, columnspan= 3)
        
        
        
        self.root.mainloop()
    
    def texto_enunciado(self, texto, consultas): 
        if self.ejercicio.get() == 0:
            self.salida.delete('1.0', 'end')
            self.salida.insert('1.0' ,texto[0][1])
            self.ejercicio.set(self.ejercicio.get()+1)
            self.r_5.config(text= 'Ejercicio nº: {}'.format(self.ejercicio.get())) 
            self.num_ejercicios.set(consultas[0])
            self.r_6.config(text= 'Nº de ejercicios: {}'.format(self.num_ejercicios.get()))
            self.sld.set(texto[0][2])
        else:
            self.salida.delete('1.0', 'end')
            self.salida.insert('1.0' ,texto[self.ejercicio.get()-1][1])
            self.sld.set(texto[self.ejercicio.get()-1][2])
                
    def nba_s(self):
        db_1 = Db()
        enunciado = db_1.nba_simple()
        consultas = db_1.nba_simple_num()
        self.texto_enunciado(enunciado, consultas)
    
    def nba_sc(self):
        db_1 = Db()
        enunciado = db_1.nba_subconsulta()
        consultas = db_1.nba_subconsulta_num()
        self.texto_enunciado(enunciado, consultas)
        
    def nba_c(self):
        db_1 = Db()
        enunciado = db_1.nba_compuesta()
        consultas = db_1.nba_compuesta_num()
        self.texto_enunciado(enunciado, consultas)
        
    def jardineria_s(self):
        db_1 = Db()
        enunciado = db_1.jardineria_simple()
        consultas = db_1.jardineria_simple_num()
        self.texto_enunciado(enunciado, consultas)
    
    def jardineria_sc(self):
        db_1 = Db()
        enunciado = db_1.jardineria_subconsulta()
        consultas = db_1.jardineria_subconsulta_num()
        self.texto_enunciado(enunciado, consultas)
        
    def jardineria_c(self):
        db_1 = Db()
        enunciado = db_1.jardineria_compuesta()
        consultas = db_1.jardineria_compuesta_num()
        self.texto_enunciado(enunciado, consultas)
    
    def enunciado(self):
        bd = self.opcion_1.get()
        query_tipo = self.opcion_2.get()
        
        if bd == 1 and query_tipo == 1:
            self.nba_s()    
        elif bd == 1 and query_tipo == 2:
            self.nba_sc()
        elif bd == 1 and query_tipo == 3:
            self.nba_c()
        elif bd == 2 and query_tipo == 1:
            self.jardineria_c()
        elif bd == 2 and query_tipo == 2:
            self.jardineria_sc()
        elif bd == 2 and query_tipo == 3:
            self.jardineria_c()
    
    def boton_siguiente(self):
        if self.ejercicio.get() < self.num_ejercicios.get():            
            self.ejercicio.set(self.ejercicio.get() + 1)
            self.r_5.config(text= 'Ejercicio nº: {}'.format(self.ejercicio.get()))
            self.salida.delete('1.0', 'end')
            self.salida_s.delete('1.0', 'end')
            self.enunciado()
                   
    def boton_atras(self):
        if self.ejercicio.get() > 1 and self.ejercicio.get() <= self.num_ejercicios.get():
            self.ejercicio.set(self.ejercicio.get() - 1)
            self.r_5.config(text= 'Ejercicio nº: {}'.format(self.ejercicio.get()))
            self.salida.delete('1.0', 'end')
            self.salida_s.delete('1.0', 'end')
            self.enunciado()
            
    def solucion(self):
        if self.ejercicio.get() > 0:
            self.salida_s.delete('1.0', 'end')
            self.salida_s.insert('1.0', self.sld.get())    

        
        
        
           
    
        