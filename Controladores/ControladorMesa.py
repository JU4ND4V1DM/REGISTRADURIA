from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self): #constructor
        print("Creando ControladorMesa")
        self.RepMesa=RepositorioMesa()
    def CrearMesa(self,RecibeMesa):#BodyRequest
        print("Creando Mesa")
        NuevaMesa=Mesa(RecibeMesa)
        self.RepMesa.save(NuevaMesa)
        return NuevaMesa.__dict__

    def BuscarMesa(self,numero):
        print("Buscando un Mesa con numero ",numero)
        laMesa = self.RepMesa.findById(id)
        return laMesa.__dict__

    def BuscaAllMesas(self):
        print("Buscando Mesas")
        return self.RepMesa.findAll()

    def update(self,RecibeMesa):
        print("Actualizando Mesa")
        UpdateMesa = Mesa(self.RepMesa.findById(RecibeMesa["idObject"]))
        UpdateMesa.numero=RecibeMesa["numero"]
        UpdateMesa.Cantidad_inscritos = RecibeMesa["cantidad de inscritos"]
        self.RepMesa.save(UpdateMesa)
        return

    def delete(self,numero):
        print("Elimiando mesa numero ",numero)
        laMesa = self.RepMesa.delete(numero)
        return True
