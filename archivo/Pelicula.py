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
        return self.Dato.anio
    
    def ObtenerGenero(self):
        return self.Dato.genero
    
    def pritt(self):
        return str(self.Dato.nombre)+"-"+str(self.Dato.actores[1])