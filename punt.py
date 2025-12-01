def compra_total(subtotal):
    iva = subtotal*0.19
    return iva
subtotal = float(input("ingrese el valor de su compra: "))
valor_iva = compra_total(subtotal)
print (f"el valor del iva de su compra es {valor_iva}")
