import csv
from colorama import Fore
import graphviz
from ListaPeliculas import ListaPeliculas
from Pelicula import Pelicula

#Lista de personas
mi_peliculas = ListaPeliculas()


# leer los archivos csv
# with open(<<nombrearchivo.extension>>, <<modo de lectura>>)
# as <<nombre de variable donde se guarda el archivo>>
# delimiter para definir como se separan las columnas
# se obtiene cada linea con la funcion reader

   # r -> indica el modo lectura 
#reader  -> iterable de lineas
# next(reader, None)  # para ignorar el encabezado 

# ruta = input("|\tIngrese la direccion del archivo de entrada: ")

#abre el archivo modo escritura
archivo = open('datos.lfp', 'r') 

#contador de cuantas lineas tiene
contadorlineas = 0
for row in open('datos.lfp') :
    contadorlineas += 1     #recuento de lineas 

for row in range(contadorlineas):
    lectura = archivo.readline().split(';')
    name = lectura[0]
    actor = lectura[1].split(',')
    lansamiento = lectura[2]
    categoria = lectura[3]
    
    #Rellenando la lista 
    mi_peliculas.IncertarPelicula(name, actor, lansamiento,categoria)  




#    mi_peliculas.IncertarPelicula(name,actor,lansamiento,categoria) 
# print("Peliculas sin ordenar") 
# print(mi_peliculas.Imprimir())
print("\n")
# print("peliculas con criterios")
print(mi_peliculas.Imprimir())

#     newPersona = Persona(name, department, birthday_month)
#     people.append(newPersona)  
# newPelicula.get_actores()

# for peli in peliculas:
#     peli.get_actores()






# while True:
#     try:
#         print(Fore.CYAN + '----------------------------------------------------')
#         print(Fore.CYAN + '|              BIENVEDIO AL PROGRAMA               |')
#         print(Fore.CYAN + '|                                                  |')
#         print(Fore.CYAN + '| Lenguajes Formales y de Programacion - Seccion A-|')
#         print(Fore.CYAN + '| Jhonatan Alexander Aguilar Reyes     - 202106003 |')
#         print(Fore.CYAN + '|                                                  |')
#         print(Fore.CYAN + '----------------------------------------------------')
#         input(Fore.CYAN + '\nPresione ENTER para contuniar')

#         while True:
#             print("----------------------------------------------------")
#             print("|                    MENU PRINCIPAL                |")
#             print("|                                                  |")
#             print("|    [1]. Cargar archivo de entrada                |")
#             print("|    [2]. Gestionar peliculas                      |")
#             print("|    [3]. Filtrado                                 |")
#             print("|    [4]. Grafica                                  |")
#             print("|    [5]. Salir                                    |")
#             print("|                                                  |")
#             print("----------------------------------------------------")
#             menu_principal_str = input("Ingrese un valor para seleccionar una opcion: ")
#             menu_principal = int(menu_principal_str)    #Parseando opcion 

#             if menu_principal == 1:   #Opcion 1 del menu principal
#                 print("\n\tUsted acaba de ingresar a la opcion 1")
#                 ruta = input("|\tIngrese la direccion del archivo de entrada: ")

#                 #abre el archivo modo escritura
#                 archivo = open(ruta, 'r') 

#                 #contador de cuantas lineas tiene
#                 contadorlineas = 0
#                 for row in open(ruta) :
#                     contadorlineas += 1     #recuento de lineas 
                
#                 for row in range(contadorlineas):
#                     lectura = archivo.readline().split(';')
#                     name = lectura[0]
#                     actor = lectura[1]
#                     lansamiento = lectura[2]
#                     categoria = lectura[3]

#                     #Rellenando la lista 
#                     mi_peliculas.IncertarPelicula(name, actor, lansamiento,categoria)                

#             if menu_principal == 2:     #Opcion 2 del menu principal
#                 while True:
#                     print("\n\nUsted se encuentra en la opcion 2")
#                     print("----------------------------------------------------")
#                     print("|              ¿Que desea realizar?                |")
#                     print("|                                                  |")
#                     print("|    [a]. Ver las peliculas registrada             |")
#                     print("|    [b]. Ver los actores de las peliculas         |")
#                     print("|    [c]. Salir de este sub-menu                   |")
#                     print("|                                                  |")
#                     print("----------------------------------------------------")
#                     menu_2 = input("Ingrese una opcion:  ")

#                     if menu_2 == "a":       #Opcion 1 del sebmenu2
#                         print("selecciono la primera opcion")

#                     if menu_2 == "b":       #Opcion 2 del sebmenu2
#                         print("selecciono la segunda opcion")
                    
#                     if menu_2 == "c":       #Opcion 3 del sebmenu2
#                         print("Nos vemos en el menu principal :)") 
#                         break 

#             if menu_principal == 3:     #Opcion tres del menu Principal
#                 while True:
#                     print("\n\nUsted se encuentra en la opcion 3")
#                     print("----------------------------------------------------")
#                     print("|              ¿Que desea realizar?                |")
#                     print("|                                                  |")
#                     print("|    [a]. Filtrar por actor                        |")
#                     print("|    [b]. Filtrar por año de estreno               |")
#                     print("|    [c]. Filtrar por genero                       |")
#                     print("|    [d]. Salir de este sub-menu                   |")
#                     print("|                                                  |")
#                     print("----------------------------------------------------")
#                     menu_3 = input("Ingrese una opcion:  ")

#                     if menu_3 == "a":       #Opcion 1 del sebmenu3
#                         print("Usted selecciono la primer opcion")

#                     if menu_3 == "b":       #Opcion 2 del sebmenu3
#                         print("Ustede selecciono la segunda opcion")

#                     if menu_3 == "c":       #Opcion 3 del sebmenu3
#                         print("Usted selecciono la tercer opcion")
                    
#                     if menu_3 == "d":       #Opcion 4 del sebmenu3
#                         print("NOs vemos en el menuPrincipal :)")
#                         break
                    
#             if menu_principal == 4:     #Opcion 4 del menu princiapal
#                 print("Usted se encuentra en la opcion 4")    

#             if menu_principal == 5:        #if que simula el do-while
#                 print("Fin del programa ;(")
#                 break
#     except:
#         print("\n\nSe acaba de producir un error :( ")
#         print("Asegurate de leer el MANUAL DE USUARIO")
#     else:
#         break