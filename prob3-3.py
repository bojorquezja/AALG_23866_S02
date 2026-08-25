x=float(input("Ingrese el valor de x: ")) 
n= int(input("Ingrese la cantidad de número que desea sumar: ")) 
terminos = [] 
suma = 0 
for i in range(n): 
    factorial = 1 
    for j in range(1, i + 1): 
        factorial *= j 
    potencia = 1 
    for k in range(1, i + 1): 
        potencia *= x 
    termino = potencia / factorial 
    terminos = terminos + [termino] 
    suma += termino
    print(f"Termino {i}: {termino:.2f}") 
print(f"\nLos {n} términos son: {terminos}") 
print(f"\nLa suma de los {n} términos es: {suma:.2f}")