horas = float(input("Ingrese las horas trabajadas: ")) 
valor_hora =float(input("Ingrese el valor de la hora: ")) 
sueldo_bruto = horas * valor_hora 
descuento = sueldo_bruto * 0.05 
sueldo_neto = sueldo_bruto - descuento 
print("Sueldo bruto: S/.", sueldo_bruto) 
print("Descuento AFP: S/.", descuento) 
print("Sueldo neto: S/.", sueldo_neto)