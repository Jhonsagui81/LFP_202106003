class Pelicula:
    def __init__(self, nombre, actores, anio, genero):
        self.nombre = nombre
        self.actores = actores
        self.anio = anio
        self.genero = genero

class NodoPelicula:
    def __init__(self, nombre, actores, anio, genero):
        self.Dato = Pelicula(nombre, actores, anio, genero)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerPelicula(self):
        return self.Dato.nombre
    
    def ObtenerActor(self):
        return self.Dato.actores

    def ObtenerAnio(self):
        lanza = self.Dato.anio.strip()
        return lanza
    
    def ObtenerGenero(self):
        gene = self.Dato.genero.strip()
        return gene
    
    def prittInforMenu2a(self):
        return str(self.Dato.nombre)+ " - Fue estrenada en "+str(self.Dato.anio)+" - Se categorizo como: "+str(self.Dato.genero)

    def prittInfoMenu2b(self):
        acrto1 = ""
        for i in self.Dato.actores:
            acrto1 += " - "+i
        return str(acrto1)
    
    def BuscarActor(self, name):
        for i in self.Dato.actores:
            sin_espacion = i.strip()
            if name == sin_espacion:
                return str(sin_espacion)