from Pelicula import NodoPelicula
from colorama import Fore

class ListaPeliculas:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    #Verifica cuantos nodos hay en la lista
    def ContarNodos(self):
        return self.Limite
    
    #Valida e inserta Nuevos nodos
    def IncertarPelicula(self, nombre, actores, anio, genero):
        NuevoNodo = NodoPelicula(nombre, actores, anio, genero)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else: #and self.Inicio.Siguiente != None
            numero = 0
            Actual = self.Inicio
            bandera = False
            while Actual != None:
                numero += 1
                if NuevoNodo.ObtenerPelicula() == Actual.ObtenerPelicula():
                    print(str("\tLa pelicula "+str(numero)+" se encuentra repetida"))
                    bandera = True
                    Actual = Actual.Siguiente
                else:
                    Actual = Actual.Siguiente 
            
            if bandera == False:
                self.Limite += 1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo 

    ##Devuelve una cadena con la informacion de las peliculas
    def ImprimirInfoPelicula(self):
        if self.Inicio == None:
            return Fore.RED+"""\n\tNo hay peliculas cargadas en el sistema
    Puede realizarlo en la opcion [1] del MENU PRINCIPAL"""
        c_pelicula = 0
        Retorno = ""
        Auxiliar = self.Inicio
        while Auxiliar != None:
            c_pelicula +=1
            Retorno += "-->La pelicula ["+str(c_pelicula)+"] es "+str(Auxiliar.prittInforMenu2a())
            if Auxiliar.Siguiente != None:
                Retorno += "\n"
            Auxiliar = Auxiliar.Siguiente
            Retorno += ""
        return Retorno
    
    ##Devuelve una cadena con los actores de cierta pelicula 
    def ImprimirActores(self, indice):
        try:
            posicion = int(indice)
        except Exception as er:
            text = Fore.RED+"\n\tOcurrio un error con la entrada, de tipo: "+str(er)
            return text+Fore.RED+"\n\tAsegurate de leer el MANUAL DE USUARIO :)"

        if self.Inicio == None:
            return +Fore.RED+"\nNo se encuentra cargada ninguna pelicula!"
        c_pelicula = 1
        Retorno = ""
        Auxiliar = self.Inicio
        if posicion == 1 :
            Retorno += "\nLa pelicula es protagonizada por: "+Fore.LIGHTMAGENTA_EX+str(Auxiliar.prittInfoMenu2b())
            return Retorno
        
        Auxiliar = Auxiliar.Siguiente
        while Auxiliar != None:
            c_pelicula += 1
            if c_pelicula == posicion:
                Retorno += "\nLa pelicula es protagonizada por: "+Fore.LIGHTMAGENTA_EX+str(Auxiliar.prittInfoMenu2b())
                return Retorno
            else:
                Auxiliar = Auxiliar.Siguiente
        else:
            return Fore.RED+"\n\tEste indice no se encuentra almacenado :("

    ##Realiza una busqueda por actor que se haya pasado como parametro
    def FiltroActor(self, item):
        item1 = item.strip()
        try:
            actor = int(item)
        except Exception as err:
            print("")
        else:
            text = Fore.RED+"\n\tNo puedes ingresar numeros aqui"
            return text + Fore.RED+"\n\tAsegurate de leer el MANUAL DE USUARIO :("
        #Fuera de las exepciones viene lo bueno xd
        Retorno = "\nEl actor "+item1+" Participa en: \n"
        Auxiliar = self.Inicio
        if item1 == Auxiliar.BuscarActor(item1):
            Retorno += Fore.LIGHTMAGENTA_EX+"-->"+str(Auxiliar.ObtenerPelicula())+"\n"

        Auxiliar = Auxiliar.Siguiente
        while Auxiliar != None:
            if item1 == Auxiliar.BuscarActor(item1):
                Retorno += Fore.LIGHTMAGENTA_EX+"-->"+str(Auxiliar.ObtenerPelicula())+"\n"
            
            Auxiliar = Auxiliar.Siguiente
        return Retorno
    
    ## Realiza una busqueda por anio y mostrara el nombre y el genero de la pelicula 
    def FiltroAnio(self, ano):
        anio = ano.strip()
        try:
            aux = int(anio)
        except:
            text = Fore.RED+"\n\tNo puedes ingresar caracteres aqui"
            return text+Fore.RED+"\n\tAsegurate de leer el MANUAL DE USUARIO :)"
        #Fuera de excepcion biene filtro
        Retorno = "\nLas peliculas lanzadas en "+str(anio)+" fueron: \n"
        Auxiliar = self.Inicio
        if anio == Auxiliar.ObtenerAnio():
            Retorno += Fore.LIGHTMAGENTA_EX+"--> "+str(Auxiliar.ObtenerPelicula())+", Genero: "+str(Auxiliar.ObtenerGenero())+"\n"

        Auxiliar = Auxiliar.Siguiente
        while Auxiliar != None:
            if anio == Auxiliar.ObtenerAnio():
                Retorno += Fore.LIGHTMAGENTA_EX+"--> "+str(Auxiliar.ObtenerPelicula())+", Genero: "+str(Auxiliar.ObtenerGenero())+"\n"
            Auxiliar = Auxiliar.Siguiente
        return Retorno
    
    ##Realiza una busqueda por genero y devuelve las peliculas con ese genero 
    def FiltroGenero(self, genero):
        genero1 = genero.strip()
        try:
            actor = int(genero)
        except Exception as err:
            print("")
        else:
            text = Fore.RED+"\n\tNo puedes ingresar numeros aqui"
            return text + Fore.RED+"\n\tAsegurate de leer el MANUAL DE USUARIO :("
        Retorno = "\nLas peliculas de "+str(genero1)+" registradas son: \n"
        Auxiliar = self.Inicio
        if genero1 == Auxiliar.ObtenerGenero():
            Retorno += Fore.LIGHTMAGENTA_EX+"-->"+str(Auxiliar.ObtenerPelicula())+"\n"
        
        Auxiliar = Auxiliar.Siguiente
        while Auxiliar != None:
            if genero1 == Auxiliar.ObtenerGenero():
                Retorno += Fore.LIGHTMAGENTA_EX+"-->"+str(Auxiliar.ObtenerPelicula())+"\n"
            Auxiliar = Auxiliar.Siguiente
        return Retorno