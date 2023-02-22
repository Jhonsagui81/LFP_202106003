from Pelicula import NodoPelicula

class ListaPeliculas:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def IncertarPelicula(self, nombre, actores, anio, genero):
        NuevoNodo = NodoPelicula(nombre, actores, anio, genero)
        self.Limite += 1
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
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo 

    def insertar(self, nombre, actores, anio, genero):
        NuevoNodo = NodoPelicula(nombre, actores, anio, genero)
        self.Limite += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def Imprimir(self):
        Retorno = "La lista tiene:["
        if self.Inicio == None:
            return "La lista esta vacia. "
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += str(Auxiliar.pritt())
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += " ]"
        return Retorno

    def ImprimirInfoPelicula(self):
        if self.Inicio == None:
            return """\n\tNo hay peliculas cargadas en el sistema
    Puede realizarlo en la opcion [1] del MENU PRINCIPAL"""
        c_pelicula = 0
        Retorno = ""
        Auxiliar = self.Inicio
        while Auxiliar != None:
            c_pelicula +=1
            Retorno += "-->La pelicula ["+str(c_pelicula)+"] es "+str(Auxiliar.prittInforMenu2())
            if Auxiliar.Siguiente != None:
                Retorno += "\n"
            Auxiliar = Auxiliar.Siguiente
            Retorno += ""
        return Retorno
        



        # Retorno = "La pelicula ["+str(self.Limite)+"] es "
        # if self.Inicio == None:
        #     return """\n\tNo hay peliculas cargadas en el sistema
        #     Puede realizarlo en la opcion [1] del MENU PRINCIPAL"""
        # Auxiliar = self.Inicio
        # while Auxiliar != None:
        #     Retorno += str(Auxiliar.prittInforMenu2)
        #     if Auxiliar.Siguiente != None:
        #         Retorno +=
