cand1 = 0 
cand2 = 0 
cand3 = 0 
cand4 = 0 
total_votos = 0 
dato = -1 
while dato != 0: 
    print("Ingrese un número de candidato (1-4) o 0 para salir:") 
    dato = int(input()) 
    if dato != 0: 
        total_votos += 1 
        match dato: 
            case 1: 
                cand1 += 1 
            case 2: 
                cand2 += 1 
            case 3: 
                cand3 += 1 
            case 4: 
                cand4 += 1
        
print("\n*** RESULTADOS DE LA VOTACIÓN ***") 
print("Total de votos: ", total_votos) 
print(f"Votos del candidato 1: {cand1} y su porcentaje fue ({(cand1/total_votos)*100:.2f}%)") 
print(f"Votos del candidato 2: {cand2} y su porcentaje fue ({(cand2/total_votos)*100:.2f}%)") 
print(f"Votos del candidato 3: {cand3} y su porcentaje fue ({(cand3/total_votos)*100:.2f}%)") 
print(f"Votos del candidato 4: {cand4} y su porcentaje fue ({(cand4/total_votos)*100:.2f}%)")