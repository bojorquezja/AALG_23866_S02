print("*** REGISTRO DEL TRABAJADOR ***\n") 
horas_trabajadas = int(input("Ingrese las horas trabajadas: ")) 
valor_por_hora = float(input("Ingrese el valor por hora: ")) 
decision = input("¿Cuenta con AFP? (si/no): ").lower() 
afp = 0 
salario_bruto = horas_trabajadas * valor_por_hora 
if decision == "si": 
    afp = salario_bruto * 0.05 
print("\n*** RESULTADOS ***") 
print(f"Salario bruto: S/{salario_bruto}") 
print(f"Descuento por AFP: S/{afp}") 
print(f"Salario neto: S/{salario_bruto - afp}")