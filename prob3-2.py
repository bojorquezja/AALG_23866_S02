num = float(input("Ingrese el valor: ")) 
n = int(input("Ingrese la cantidad de términos: ")) 
suma = 0 
factorial = 1 
potencia = 1 
for i in range(n): 
    if i > 0: 
        potencia = potencia * num 
        factorial = factorial * i 
    termino = potencia / factorial 
    suma = suma + termino 
print("La suma es:", suma)