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

import sqlite3

class Libreria:
    def __init__(self):
        self.conexion = Conexiones()
        self.conexion.abrirConexion()
        self.conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        self.conexion.miCursor.execute("CREATE TABLE LIBROS (id_libro INTEGER PRIMARY KEY, titulo VARCHAR(30), autor VARCHAR(30), precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL, UNIQUE(titulo, autor))")
        self.conexion.miConexion.commit()
    
    def agregar_libro(self, titulo, autor, precio, cantidadDisponibles):
        try:
            self.conexion.miCursor.execute("INSERT INTO LIBROS (titulo, autor, precio, cantidadDisponibles) VALUES (?, ?, ?, ?)", (titulo, autor, precio, cantidadDisponibles))
            self.conexion.miConexion.commit()
            print("Libro agregado exitosamente")
        except:
            print("Error al agregar un libro")
    
    def modificar_libro(self, titulo, autor, precio):
        try:
            self.conexion.miCursor.execute("UPDATE LIBROS SET precio = ? WHERE titulo = ? AND autor = ?", (precio, titulo, autor))
            self.conexion.miConexion.commit()
            print("Libro modificado correctamente")
        except:
            print("Error al modificar un libro")
    
    def cerrar_libreria(self):
        self.conexion.cerrarConexion()

class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Libreria.db")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()  


libreria = Libreria()

while True:
    print("Menu de opciones Libreria")
    print("1- Agregar libro")
    print("2- Modificar libro")
    print("0- Salir del menú")
    
    opcion = int(input("Por favor ingrese un número: "))
    
    if opcion == 1:
        titulo = input("Por favor ingrese el título del libro: ")
        autor = input("Por favor ingrese el autor del libro: ")
        precio = float(input("Por favor ingrese el precio del libro: "))
        cantidadDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
        libreria.agregar_libro(titulo, autor, precio, cantidadDisponibles)
    elif opcion == 2:
        titulo = input("Por favor ingrese el título del libro a modificar: ")
        autor = input("Por favor ingrese el autor del libro a modificar: ")
        precio = float(input("Por favor ingrese el nuevo precio del libro: "))
        libreria.modificar_libro(titulo, autor, precio)
    elif opcion == 0:
        libreria.cerrar_libreria()
        break