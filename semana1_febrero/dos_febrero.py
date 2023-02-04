"""
    Programa1
    Nombre:Amayrani DB
    Fecha: 2/02/23
    Descripcion: Mostrar el precio iva de un producto con valor     de 670 y su precio final
"""

iva = 0.30  #da el valor al iva
precioproducto = 670  #da el valor de precio al producto
precioiva = precioproducto * iva  #hace la multiplicacion de precio producto por el iva y calcula el precio iva
print("El precio del IVA es: ",precioiva)  #imprime el precio iva
print("El precio final es: ", (precioiva + precioproducto) )  #imprime el precio final de el precio del iva mas el precio del producto
