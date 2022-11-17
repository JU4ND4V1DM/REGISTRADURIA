from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorCandidato():
    def __init__(self): #constructor
        print("Creando ControladorCandidato")
        self.RepCandidato=RepositorioCandidato()
    def CrearCandidato(self,RecibeCandidato):#BodyRequest
        print("Creando Candidato")
        NuevoCandidato=Candidato(RecibeCandidato)
        self.RepCandidato.save(NuevoCandidato)
        return NuevoCandidato.__dict__

    def BuscarCandidato(self,id):
        print("Buscando un Candidato con id ",id)
        elCandidato = self.RepCandidato.findById(id)
        return elCandidato.__dict__

    def BuscaAllCandidatos(self):
        print("Buscando Candidatos")
        return self.RepCandidato.findAll()

    def update(self,RecibeCandidato):
        print("Actualizando Candidato")
        UpdateCandidato = Candidato(self.RepCandidato.findById(RecibeCandidato["idObject"]))
        UpdateCandidato.cedula=RecibeCandidato["cedula"]
        UpdateCandidato.numResolucion = RecibeCandidato["numero de resolucion"]
        UpdateCandidato.nombre = RecibeCandidato["nombre"]
        UpdateCandidato.apellido = RecibeCandidato["apellido"]
        self.RepCandidato.save(UpdateCandidato)
        return

    def delete(self,id):
        print("Elimiando Candidato con id ",id)
        elCandidato = self.RepCandidato.delete(id)
        return True
