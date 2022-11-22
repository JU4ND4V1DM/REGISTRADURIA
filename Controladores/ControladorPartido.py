from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorPartido():
    def __init__(self): #constructor
        print("Creando ControladorPartido")
        self.RepPartido=RepositorioPartido()
    def CrearPartido(self,RecibePartido):#BodyRequest
        print("Creando Partido")
        NuevoPartido=Partido(RecibePartido)
        self.RepPartido.save(NuevoPartido)
        return NuevoPartido.__dict__

    def BuscarPartido(self,id):
        print("Buscando un Partido con id ",id)
        elPartido = self.RepPartido.findById(id)
        return elPartido.__dict__

    def BuscarAllPartidos(self):
        print("Buscando Partidos")
        return self.RepPartido.findAll()

    def update(self,RecibePartido):
        print("Actualizando Partido")
        UpdatePartido = Partido(self.RepPartido.findById(RecibePartido["idObject"]))
        UpdatePartido.id=RecibePartido["id"]
        UpdatePartido.nombre = RecibePartido["nombre"]
        UpdatePartido.slogan = RecibePartido["slogan"]
        self.RepPartido.save(UpdatePartido)
        return

    def delete(self,id):
        print("Elimiando Partido con id ",id)
        elPartido = self.RepPartido.delete(id)
        return True
