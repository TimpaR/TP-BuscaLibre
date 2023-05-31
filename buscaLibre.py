import sqlite3
from datetime import datetime

class buscaLibre:

    def menu(self):
        while True:
            print("Menu de opciones BuscaLibre")
            print("1- Cargar Libros")
            print("2- Modificar precio de un libro")
            print("3- Borrar un libro")
            print("4- Cargar cantidad")
            print("5- Listado de libros")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
            # De cada libro se quiere saber ID, ISBN, Título, Autor, Género, Precio, FechaUltimoPrecio y CantDisponible.
            if nro == 1:
                id = int(input("Por favor ingrese el ID: "))
                isbn = int(input("Por favor ingrese el ISBN: "))
                titulo = str(input("Por favor ingrese el titulo: "))
                autor = str(input("Por favor ingrese el autor: "))
                genero = str(input("Por favor ingrese el género: "))
                precio = float(input("Por favor ingrese el precio: "))
                fecha = datetime.now()
                cantidad = int(input("Por favor ingrese la cantidad: "))
                nuevo_libro = Libro(id,isbn,titulo,autor,genero,precio,fecha,cantidad)
                nuevo_libro.cargar_libro()
            if nro == 2:
                
            if nro == 3:
                
            if nro == 4:
                 
            if nro == 5:
                 
            if nro == 0:
                break
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS LIBRO")
        conexion.miCursor.execute("CREATE TABLE LIBRO (id INTEGER PRIMARY KEY , isbn INTEGER , titulo  VARCHAR(50) ,autor  VARCHAR(50),genero VARCHAR(30), precio FLOAT NOT NULL,fecha VARCHAR(15) , cantidad INTEGER NOT NULL,UNIQUE(id,isbn))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()





"""           if nro == 1:
                CargarLibro()
            if nro == 2:
                ModPrecio()
            if nro == 3:
                BorrarLibro()
            if nro == 4:
                CargaCantidad()
            if nro == 5:
                Listado()
            if nro == 0:
                break

class CargarLibro:
   id = int(input("Por favor ingrese el ID: "))
   isbn = int(input("Por favor ingrese el ISBN: "))
   titulo = str(input("Por favor ingrese el titulo: "))
   autor = str(input("Por favor ingrese el autor: "))
   genero = str(input("Por favor ingrese el género: "))
   precio = float(input("Por favor ingrese el precio: "))
   fecha = datetime.now()
   def __init__(self, id: int, isbn: int, titulo: str, autor: str, genero: str, precio: float, fecha) -> None:
        self.id = id
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.fecha = fecha
class ModPrecio:
    buquedaId = input(int()
class BorrarLibro:

class CargaCantidad:

class Listado:"""

