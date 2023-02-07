"""
    Programa 5
    Nombre:Amayrani DB
    Fecha: 6/02/23
    Descripcion: Determinar si un estudiante aprobo la materia o la reprobo pidiendo 3 calicficaciones
"""
calif1 = float(input("Ingresa la primera calificacion : "))  #pedira la calificacion de la primera materia
calif2 = float(input("Ingresa la segunda calificacion: "))  #pedira la calificacion de la segunda materia
calif3 = float(input("Ingresa la tercera calificacion: "))  #pedira la calificacion de la tercera materia

promedio = (calif1 + calif2 + calif3) / 3

if promedio >= 7:  #dice si tu promedio es mayor o igual a 7
    print("Felicidades aprobaste la materia con el promedio de: ", promedio) #va a imprir que eres aprobado en la materia

else:  #da una condicion si no
    print("Lo sentimos reprobaste la materia con el promedio de: ",promedio)  #va a imprimir que reprobo la materia