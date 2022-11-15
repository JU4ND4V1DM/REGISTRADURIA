from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self): #constructor
        print("Creando ControladorCandidato")
    def index(self):
        print("Listar todos los Candidatos")
        unCandidato={
            "_id":"abc123",
            "cedula":"123",
            "nombre":"Juan",
            "apellido":"Perez"
        }
        return [unCandidato]
    def create(self,infoCandidato):
        print("Crear un Candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__
    def show(self,id):
        print("Mostrando un Candidato con id ",id)
        elCandidato = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elCandidato
    def update(self,id,infoCandidato):
        print("Actualizando Candidato con id ",id)
        elCiudadano = Candidato(infoCandidato)
        return elCiudadano.__dict__
    def delete(self,id):
        print("Elimiando Candidato con id ",id)
        return {"deleted_count":1}