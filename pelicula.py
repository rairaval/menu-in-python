#tengo que poner algo para que me aparezcan las peliculas
#from catalogo import*
#from menu import*

class Pelicula:
    #constructor de clase
    def __init__(self,titulo,duracion,lanzamiento,director,genero):
            self.titulo=titulo
            self.duracion=duracion
            self.lanzamiento=lanzamiento
            self.director=director
            self.genero=genero
            print('\n Se ha creado la pelicula: {}'.format(self.titulo))
    #redefinamos el metodo sting
    def __str__(self):
            return '{} ({}, {} - {})'.format(self.titulo, self.lanzamiento, self.duracion, self.genero)

    def __del__(self):
            return 'Se	está	borrando	la	película {}'.format(self.titulo)
