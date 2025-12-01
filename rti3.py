def total_venta (valor_u, cantidad_v):
    return valor_u * cantidad_v
valor_u = float(input("ingrese el valor unitario del producto:"))
cantidad_v = int(input("ingrese la cantidad de productos vendidos: "))
print(f"el total de la venta es: {total_venta(valor_u, cantidad_v)}")