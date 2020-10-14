from pelicula import *
#from menu import * #lo puedo sacar

class Catalogo:
    peliculas = []
    def __init__(self,peliculas=[]):
            self.peliculas=peliculas

    def agregar(self,p):
            self.peliculas.append(p)

    def agregar_pelicula(self):
        while True:
            try:
                titulo= input('Intorduzca un titulo:'.capitalize())
                duracion= float(input('Introduzca una duracion en minutos: '))
                lanzamiento= float(input('Introduzca un anio de lanzamiento: '))
                director= input('Introduzca el nombre del director: ').capitalize()
                genero= input('Introduzca el genero: ').capitalize()
                nueva_pelicula = Pelicula (titulo, duracion, lanzamiento, director, genero)
                self.peliculas.append (nueva_pelicula)
                return #Pelicula(titulo, duracion, lanzamiento, director, genero)

            except TypeError:
                print('\nintoduce correctamente los numeros\n')
                return
            except ValueError:
                print('\nintoduce correctamente los numeros\n')
                return
            else:
                print('pelicula correctamente intoducida')
                break



    def eliminar_pelicula(self):

        while True:
            try:
                numero=int(input('introduzca numero de pelicula que quiere borrar: '))
                numero=numero-1
                for i,e in enumerate(self.peliculas):
                            if numero == i:
                                    del(self.peliculas [numero])
                                    print('Pelicula {} ha sido borrada del catalogo'.format(e))
                                    return
            except ValueError:
                print('Debe introducir un numero del listado')
                return
            else:
                print('pelicula no encontrada')
                break


    def mostrar_pelicula(self):
            for i,p in enumerate (self.peliculas):
                    print(i+1,p)


    def mostrarxgenero(self, genero=None):
            genero= input('seleccione genero: ')
            print ('\n Lista de peliculas por genero {} \n'.format(genero))
            for p in self.peliculas:
                    if p.genero == genero:
                            print(p)
            else:
                            print('no hay peliculas con ese genero')
