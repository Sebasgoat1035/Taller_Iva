def ganancia (a, b):
    return a - b
cos_uni = float(input("ingrese el costo unitario del producto: "))
val_venta = float(input("ingrese el precio de venta del producto"))
print(f"la ganancia del producto es: {ganancia(val_venta, cos_uni)}")