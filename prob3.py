print("Ingrese el valor para la funcion: ") 
x = int(input()) 
print("Ingrese la cantidad de términos: ") 
n = int(input()) 
suma = 0 
factorial = 1 
for i in range(n): 
    if i > 0: 
        factorial *= (i) 
    suma += (x**i)/factorial 
print("La suma de los factoriales es:", suma)