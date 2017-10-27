
def buscaModa2(valores):
    moda = valores[0]
    indice = 0
    freq = 1
    while indice < len(valores) - 1:
        indice += 1
        if valores[indice] == valores[indice - freq]:
            moda = valores[indice]
            freq += 1
    return moda

def preencher(vetor):

    for i in range(len(vetor)):
        vetor[i] = int(input("V[" + str(i) + "]: "))
    return None

# -------------- programa principal --------------- #

N = int(input("Numero desejado de elementos: "))
numeros = [0] * N
preencher(numeros)
moda = buscaModa2(numeros)
print("Moda do vetor: %d" % moda)
