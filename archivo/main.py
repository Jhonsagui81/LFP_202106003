import csv
from Persona import Persona

#Lista de personas
people = []

# leer los archivos csv
# with open(<<nombrearchivo.extension>>, <<modo de lectura>>)
# as <<nombre de variable donde se guarda el archivo>>
# delimiter para definir como se separan las columnas
# se obtiene cada linea con la funcion reader

csvfile = open('datos.lfp', 'r')    # r -> indica el modo lectura 
reader = csv.reader(csvfile, delimiter=',')   #reader  -> iterable de lineas
next(reader, None)  # para ignorar el encabezado 

for row in reader:
    name = row[0]
    department = row[1]
    birthday_month = row[2]

    newPersona = Persona(name, department, birthday_month)
    people.append(newPersona)

# for person in people:
#     person.print_name()       mostrar info de los objetos 


print("----------------------------------------------------")
print("|              BIENVEDIO AL PROGRAMA               |")
print("|                                                  |")
print("| Lenguajes Formales y de Programacion - Seccion A-|")
print("| Jhonatan Alexander Aguilar Reyes     - 202106003 |")
print("|                                                  |")
print("----------------------------------------------------")
input("\nPresione ENTER para contuniar")

while True:
    print("----------------------------------------------------")
    print("|                    MENU PRINCIPAL                |")
    print("|                                                  |")
    print("|    [1]. Cargar archivo de entrada                |")
    print("|    [2]. Gestionar peliculas                      |")
    print("|    [3]. Filtrado                                 |")
    print("|    [4]. Grafica                                  |")
    print("|    [5]. Salir                                    |")
    print("|                                                  |")
    print("----------------------------------------------------")
    menu_principal_str = input("\nIngrese un valor para seleccionar una opcion: ")
    menu_principal = int(menu_principal_str)    #Parseando opcion 

    if menu_principal == 1:
        print("\n\nUsted acaba de ingresar a la opcion 1")
        

    if menu_principal == 2:
        while True:
            print("\n\nUsted se encuentra en la opcion 2")
            print("----------------------------------------------------")
            print("|              ¿Que desea realizar?                |")
            print("|                                                  |")
            print("|    [a]. Ver las peliculas registrada             |")
            print("|    [b]. Ver los actores de las peliculas         |")
            print("|    [c]. Salir de este sub-menu                   |")
            print("|                                                  |")
            print("----------------------------------------------------")
            menu_2 = input("Ingrese una opcion")

            if menu_2 == "a":
                print("selecciono la primera opcion")
                
            if menu_2 == "b":
                print("selecciono la segunda opcion")
            
            if menu_2 == "c":
                print("Nos vemos en el menu principal :)") 
                break 

    if menu_principal == 3:
        print("\n\nUsted se encuentra en la opcion 3")
        print("----------------------------------------------------")
        print("|              ¿Que desea realizar?                |")
        print("|                                                  |")
        print("|    [a]. Filtrar por actor                        |")
        print("|    [b]. Filtrar por año de estreno               |")
        print("|    [c]. Filtrar por genero                       |")
        print("|                                                  |")
        print("----------------------------------------------------")

    if menu_principal == 4:
        print("Usted se encuentra en la opcion 4")    

    if menu_principal == 5:        #if que simula el do-while
        print("Fin del programa ;(")
        break
