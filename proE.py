def calcular_total(subtotal):
    iva= subtotal * 0.19
    return iva 
subtotal = float(input("ingrese su subtotal: "))
print (f"iva: ${calcular_total(subtotal)}, subtotal: ${subtotal}, total: ${calcular_total(subtotal) + subtotal}")
 