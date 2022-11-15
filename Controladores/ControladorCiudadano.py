from Modelos.Candidato import Ciudadano
class ControladorCiudadano():
    def __init__(self):
        print("Creando ControladorCiudadano")
    def index(self):
        print("Listar todos los Ciudadanos")
        unCiudadano={
            "_id":"abc123",
            "cedula":"123",
            "nombre":"Juan",
            "apellido":"Perez"
        }
        return [unCiudadano]
    def create(self,infoCiudadano):
        print("Crear un Ciudadano")
        elCiudadano = Ciudadano(infoCiudadano)
        return elCiudadano.__dict__
    def show(self,id):
        print("Mostrando un Ciudadano con id ",id)
        elCiudadano = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elCiudadano
    def update(self,id,infoCiudadano):
        print("Actualizando Ciudadano con id ",id)
        elCiudadano = Ciudadano(infoCiudadano)
        return elCiudadano.__dict__
    def delete(self,id):
        print("Elimiando Ciudadano con id ",id)
        return {"deleted_count":1}