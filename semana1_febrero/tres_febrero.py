"""
    Programa2
    Nombre:Amayrani DB
    Fecha: 3/02/23
    Descripcion: Calcular la longuitud de la hipotenusa de un        triangulo rectangulo
"""

puntoab = float(input("Escriba el valor de la longitud del vertice AB: "))  #se da a que escriban el valor del punto ab
puntobc = float(input("Escriba el valor de la longitud del vertice BC: "))   # #se da a que escriban el valor del punto bc

hipotenusa = (puntoab**2 + puntobc**2)  #se saca el valor de la hipotenusa sacando el cuadrado del punto ab y punto bc
print("La longitud de la hipotenusa es: ",hipotenusa)  #se imprime en la pantalla la longitud de la hipotenusa