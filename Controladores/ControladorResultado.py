from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado


class ControladorResultado():
    def __init__(self): #constructor
        print("Creando ControladorResultado")
        self.RepResultado=RepositorioResultado()
    def CrearResultado(self,RecibeResultado):#BodyRequest
        print("Creando Resultado")
        NuevoResultado=Resultado(RecibeResultado)
        self.RepResultado.save(NuevoResultado)
        return NuevoResultado.__dict__

    def BuscarResultado(self,id):
        print("Buscando un Resultado con id ",id)
        elResultado = self.RepResultado.findById(id)
        return elResultado.__dict__

    def BuscaAllResultados(self):
        print("Buscando Resultados")
        return self.RepResultado.findAll()

    def update(self,RecibeResultado):
        print("Actualizando Resultado")
        UpdateResultado = Resultado(self.RepResultado.findById(RecibeResultado["idObject"]))
        UpdateResultado.id=RecibeResultado["id"]
        UpdateResultado.numMesa = RecibeResultado["numero de Mesa"]
        UpdateResultado.cedulaCandidato = RecibeResultado["numero de cedula candidato"]
        UpdateResultado.numVotos = RecibeResultado["numero de Votos"]
        self.RepResultado.save(UpdateResultado)
        return

    def delete(self,id):
        print("Elimiando Resultado con id ",id)
        elResultado = self.RepResultado.delete(id)
        return True
