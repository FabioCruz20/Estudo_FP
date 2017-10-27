

def buscaModa(valores):

    auxiliar = [0] * len(valores)
    for i in range(len(valores)):
        auxiliar[i] = 1
        for j in range(i + 1, len(valores)):
            if valores[i] == valores[j]:
                auxiliar[i] += 1

    posModa = 0
    for i in range(1, len(auxiliar)):
        if auxiliar[i] > auxiliar[posModa]:
            posModa = i

    return valores[posModa]


vetor = [10, 10, 20, 5]
moda = buscaModa(vetor)
print("Moda do vetor: %d" % moda)

#vetor.extend([20, 5, 5])
vetor = vetor + [20, 5, 5]
moda = buscaModa(vetor)
print("Moda do vetor: %d" % moda)
