"""
    Programa14
    Nombre:Amayrani DB
    Fecha: 23/02/23
    Descripcion:Clase persona escuela
"""
class Persona:
    nombre = ''
    escuela = ''

    def print_nombre(self):
        print self.nombre

    def print_escuela(self):
        print self.escuela

amayrani = Persona()
amayrani.nombre = 'Amayrani'
amayrani.escuela = 'UTEC'
amayrani.print_nombre()
amayrani.print_escuela()