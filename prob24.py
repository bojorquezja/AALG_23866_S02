votos1 = 0 
votos2 = 0 
votos3 = 0 
votos4 = 0 
voto = int(input("Ingrese voto [1-4] (0 para terminar): ")) 
while voto != 0: 
    if voto == 1: 
        votos1 += 1 
    elif voto == 2: 
        votos2 += 1 
    elif voto == 3: 
        votos3 += 1 
    elif voto == 4: 
        votos4 += 1 
    else: 
        print("ERROR: El voto debe ser 1, 2, 3 o 4") 
    voto = int(input("Ingrese voto [1-4] (0 para terminar): ")) 
    total = votos1 + votos2 + votos3 + votos4 

print("\nRESULTADOS") 
print("Candidato 1:", votos1, "votos") 
print("Candidato 2:", votos2, "votos") 
print("Candidato 3:", votos3, "votos") 
print("Candidato 4:", votos4, "votos") 
print("\nPORCENTAJES") 
print("Candidato 1:", votos1 * 100 / total, "%") 
print("Candidato 2:", votos2 * 100 / total, "%") 
print("Candidato 3:", votos3 * 100 / total, "%") 
print("Candidato 4:", votos4 * 100 / total, "%")