#nomina
def nomina (a,b,c,d,activo):
    if activo:
        return a * b - c - d 
    else:
        return 0
val_hora = float(input("ingrese el valor de la hora trabajada: "))
horas_traba = int(input("ingrese la cantidad de horas trabajadas: "))
dedu_fon = float(input("ingrese el valor de las deducciones a restar: "))
otra_dedu = float(input("ingrese el valor de las otras deducciones a restar: "))
activo = input("¿El empleado está activo? (si/no): ").lower() == "si"
print (f"el valor a pagar al empleado es: {nomina(val_hora,horas_traba,dedu_fon,otra_dedu,activo)}")    
        
        

