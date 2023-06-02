import pymysql

class Db:
    
    def abrir_conexion(self):

        try:
            conexion = pymysql.connect(user= 'root', password= 'publucas', host='127.0.0.1', database= 'consultas')
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return conexion
    
    def nba_simple(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='NBA' AND tipo='Simple'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def nba_subconsulta(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='NBA' AND tipo='Subconsulta'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def nba_compuesta(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='NBA' AND tipo='Compuesta'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_simple(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='Jardineria' AND tipo='Simple'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_subconsulta(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='Jardineria' AND tipo='Subconsulta'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_compuesta(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT ROW_NUMBER() OVER (ORDER BY id ASC),enunciado,solucion FROM ejercicios WHERE bd='Jardineria' AND tipo='Compuesta'"       
                    cursor.execute(query)
                    salida = cursor.fetchall()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def nba_simple_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='NBA' AND tipo='Simple'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def nba_subconsulta_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='NBA' AND tipo='Subconsulta'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def nba_compuesta_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='NBA' AND tipo='Compuesta'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_simple_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='Jardineria' AND tipo='Simple'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_subconsulta_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='Jardineria' AND tipo='Subconsulta'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida
        
    def jardineria_compuesta_num(self):
        cnx = self.abrir_conexion()
        
        try:
            with cnx:
                with cnx.cursor() as cursor:
                    query = "SELECT COUNT(*) FROM ejercicios WHERE bd='Jardineria' AND tipo='Compuesta'"       
                    cursor.execute(query)
                    salida = cursor.fetchone()
        except NameError:
            print('Error: {}'.format(NameError))
        else:
            return salida   
        
            