from catalogo import *
from pelicula import *


#se crea un objeto llamado Catalogo
c = Catalogo ()

c.agregar(Pelicula('El secreto de sus ojos',170,2009,'Juan Jose Campanela','Drama'))
c.agregar(Pelicula('Media noche en Paris',100,2010,'Woddy Allen','Fantasia'))
c.agregar(Pelicula('Origen', 148, 2010,'Christopher Nolan','Ciencia ficcion'))
c.agregar(Pelicula('Perfume de Mujer',156,1992,'Martin Brest','Drama'))
c.agregar(Pelicula('Memorias de una geisha',145,2005,'Rob Marshall','Drama'))
c.agregar(Pelicula('25 whatts',94,2001,' Pablo Stoll, Juan Pablo Rebella','Comedia'))
c.agregar(Pelicula('El viaje hacia el mar',90,2003,'Guillermo Casanova','Aventura'))
c.agregar(Pelicula('whisky',100,2004,'Juan Pablo Rebella, Pablo Stoll','Drama'))
c.agregar(Pelicula('La noche de 12 años',123,2018,'Álvaro Brechner','Drama'))
c.agregar(Pelicula('Lost in Translation',104,2003,'Sofia Coppola','Comedia'))
c.agregar(Pelicula('El Guerrero Pacifico',120,2006,'Victor Salva','Drama'))
c.agregar(Pelicula('Cabaret',124,1972,'Bob Fosse','Melodrama'))
c.agregar(Pelicula('Una Mente Maravillosa',140,2002,'Ron Howard','Drama'))
c.agregar(Pelicula('Infiltrados',151,2006,'Martin Scorsese','Película de misterio'))
c.agregar(Pelicula('Interestelar',109,2014,'','Película de misterio'))

#print(c)


print('\n MENU \n======\n')

while True:
    print('\nSelecciona una opcion:\n')
    print('1: Mostrar todo el catalogo de peliculas')
    print('2: Mostrar peliculas por genero')
    print('3: Añadir pelicula nueva')
    print('4: Eliminar pelicula')
    print('5: Salir\n')

    user_choice	= input('seleccione una opcion: ')

    if user_choice	== '1':
            print('\nlista de peliculas existentes\n')
            c.mostrar_pelicula()

    elif user_choice == '2':
            c.mostrarxgenero()

    elif user_choice =='3':
            print('\n Describa su pelicula \n')
            c.agregar_pelicula()

    elif user_choice =='4':
            c.mostrar_pelicula()
            print('\n Describa la pelicula \n')
            c.eliminar_pelicula()

    elif user_choice == '5':
            print('Saliendo	del	programa!')
            break
    else:
        print('Opción	no	válida,	vuelve	a	intentarlo.\n')
