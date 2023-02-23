import csv
from colorama import Fore
import graphviz
from ListaPeliculas import ListaPeliculas
from Pelicula import Pelicula

#Lista de personas
mi_peliculas = ListaPeliculas()

##Codigo para pruebas del documento

# archivo = open('datos.lfp', 'r') 

# #contador de cuantas lineas tiene
# contadorlineas = 0
# for row in open('datos.lfp') :
#     contadorlineas += 1     #recuento de lineas 

# for row in range(contadorlineas):
#     lectura = archivo.readline().split(';')
#     name = lectura[0]
#     actor = lectura[1].split(',')
#     lansamiento = lectura[2]
#     categoria = lectura[3]
    
#     #Rellenando la lista 
#     mi_peliculas.IncertarPelicula(name, actor, lansamiento,categoria)  
def CargaDeArchivo():
    try:
        print("\n\tUSTED SE ENCUENTRA EN LA OPOCION 1")
        ruta = input("-> Ingrese la direccion del archivo de entrada: ")
        
        #abre el archivo modo escritura
        archivo = open(ruta, 'r') 

        #contador de cuantas lineas tiene
        contadorlineas = 0
        for row in open(ruta) :
            contadorlineas += 1     #recuento de lineas 
        
        for row in range(contadorlineas):
            lectura = archivo.readline().split(';')
            name = lectura[0]
            actor = lectura[1].split(',')
            lansamiento = lectura[2]
            categoria = lectura[3]
        
            #Rellenando la lista 
            mi_peliculas.IncertarPelicula(name, actor, lansamiento,categoria)
    except Exception as err:
        print(Fore.RED+"\n\tOcurrio un error con la carga del archivo :| del tipo: "+str(err))
        print(Fore.RED+"\tIntentalo de nuevo\n")
    else:
        print(Fore.GREEN+"\n\tEl archivo se cargo exitosamente :) ")

while True:
    try:
        print(Fore.CYAN + '----------------------------------------------------')
        print(Fore.CYAN + '|              BIENVEDIO AL PROGRAMA               |')
        print(Fore.CYAN + '|                                                  |')
        print(Fore.CYAN + '| Lenguajes Formales y de Programacion - Seccion A-|')
        print(Fore.CYAN + '| Jhonatan Alexander Aguilar Reyes     - 202106003 |')
        print(Fore.CYAN + '|                                                  |')
        print(Fore.CYAN + '----------------------------------------------------')
        input(Fore.CYAN + '\nPresione ENTER para contuniar')

        while True:
            print(Fore.CYAN +"----------------------------------------------------")
            print(Fore.CYAN +"|                    MENU PRINCIPAL                |")
            print(Fore.CYAN +"|                                                  |")
            print(Fore.CYAN +"|    [1]. Cargar archivo de entrada                |")
            print(Fore.CYAN +"|    [2]. Gestionar peliculas                      |")
            print(Fore.CYAN +"|    [3]. Filtrado                                 |")
            print(Fore.CYAN +"|    [4]. Grafica                                  |")
            print(Fore.CYAN +"|    [5]. Salir                                    |")
            print(Fore.CYAN +"|                                                  |")
            print(Fore.CYAN +"----------------------------------------------------")
            menu_principal_str = input(Fore.CYAN +"Ingrese un valor para seleccionar una opcion: ")
            menu_principal = int(menu_principal_str)    #Parseando opcion 

            if menu_principal == 1:   #Opcion 1 del menu principal
                CargaDeArchivo()    #funcion para cargar archivo

            if menu_principal == 2:     #Opcion 2 del menu principal
                while True:
                    print(Fore.CYAN +"\n\nUsted se encuentra en la opcion 2")
                    print(Fore.CYAN +"----------------------------------------------------")
                    print(Fore.CYAN +"|              ¿Que desea realizar?                |")
                    print(Fore.CYAN +"|                                                  |")
                    print(Fore.CYAN +"|    [a]. Ver las peliculas registrada             |")
                    print(Fore.CYAN +"|    [b]. Ver los actores de las peliculas         |")
                    print(Fore.CYAN +"|    [c]. Salir de este sub-menu                   |")
                    print(Fore.CYAN +"|                                                  |")
                    print(Fore.CYAN +"----------------------------------------------------")
                    menu_2 = input(Fore.CYAN+"Ingrese una opcion:  ")

                    if menu_2 == "a":       #Opcion 1 del sebmenu2
                        bandera = mi_peliculas.ContarNodos()
                        if bandera != 0:
                            print("selecciono la primera opcion\n")
                            print(Fore.YELLOW+ mi_peliculas.ImprimirInfoPelicula()) ##funcion imprimir peliculas 
                        else: 
                            print(mi_peliculas.ImprimirInfoPelicula())

                    if menu_2 == "b":       #Opcion 2 del sebmenu2
                        print("selecciono la segunda opcion\n")

                        bandera = mi_peliculas.ContarNodos()
                        if bandera != 0:
                            print(Fore.YELLOW+ mi_peliculas.ImprimirInfoPelicula())
                            indice_Pelicula = input(Fore.YELLOW+"Ingrese el numero de la pelicula de la que desea conocer sus actores: ")
                            print(mi_peliculas.ImprimirActores(indice_Pelicula))
                        else:
                            print(mi_peliculas.ImprimirInfoPelicula())
                    
                    if menu_2 == "c":       #Opcion 3 del sebmenu2
                        print(Fore.RED+"Nos vemos en el menu principal :)") 
                        break 

            if menu_principal == 3:     #Opcion tres del menu Principal
                while True:
                    print(Fore.CYAN +"\n\nUsted se encuentra en la opcion 3")
                    print(Fore.CYAN +"----------------------------------------------------")
                    print(Fore.CYAN +"|              ¿Que desea realizar?                |")
                    print(Fore.CYAN +"|                                                  |")
                    print(Fore.CYAN +"|    [a]. Filtrar por actor                        |")
                    print(Fore.CYAN +"|    [b]. Filtrar por año de estreno               |")
                    print(Fore.CYAN +"|    [c]. Filtrar por genero                       |")
                    print(Fore.CYAN +"|    [d]. Salir de este sub-menu                   |")
                    print(Fore.CYAN +"|                                                  |")
                    print(Fore.CYAN +"----------------------------------------------------")
                    menu_3 = input(Fore.CYAN +"Ingrese una opcion:  ")

                    if menu_3 == "a":       #Opcion 1 del sebmenu3
                        print(Fore.CYAN +"Usted Desea filtrar las peliculas por su actor")
                        bandera = mi_peliculas.ContarNodos()
                        if bandera != 0:
                            item = input(Fore.CYAN + "Ingrese el nombre del actor: ")
                            print(mi_peliculas.FiltroActor(item))
                            ##Pendiente
                        else:
                            print(mi_peliculas.ImprimirInfoPelicula())



                    if menu_3 == "b":       #Opcion 2 del sebmenu3
                        print("Ustede selecciono la segunda opcion")

                    if menu_3 == "c":       #Opcion 3 del sebmenu3
                        print("Usted selecciono la tercer opcion")
                    
                    if menu_3 == "d":       #Opcion 4 del sebmenu3
                        print("NOs vemos en el menuPrincipal :)")
                        break
                    
            if menu_principal == 4:     #Opcion 4 del menu princiapal
                print("Usted se encuentra en la opcion 4")    

            if menu_principal == 5:        #if que simula el do-while
                print("Fin del programa ;(")
                break
    except Exception as err:
        print(Fore.RED+"\n\tSe acaba de producir un error :( " + str(err))
        print(Fore.RED+"\tAsegurate de leer el MANUAL DE USUARIO")
    else:
        break