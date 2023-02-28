"""
    Programa14
    Nombre:Amayrani DB
    Fecha: 23/02/23
    Descripcion:Clase animal que permite procesar informacion de los animalesque se encuentran en una veterinaria
"""
class Animal:
    def __init__(self,nombre,especie,edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    #metodos accesores
    def getNombre(self):
        return self.nombre
    def getEspecie(self):
        return self.especie
    def getEdad(self):
        return self.edad

    def mostrarAnimal(self):
        print("\nNombre: " +self.getNombre()+"\nEspecie: "+self.getEspecie()+"\nEdad: " + str(self.getEdad()))


nombre = input("Ingresar tipo de animal: ")
especie = input("Ingresar especie: ")
edad = input("Ingresar edad: ")
e = Animal(nombre,especie,edad)
e.mostrarAnimal()
