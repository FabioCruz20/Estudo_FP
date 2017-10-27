
# selection sort
def ordenar(valores):
    for i in range(len(valores) - 1):
        posMenor = selecionarMenor(i, valores)
        trocar(valores, i, posMenor)
    return None
    

def selecionarMenor(inicio, valores):
    posMenor = inicio
    for i in range(inicio + 1, len(valores)):
        if valores[i] < valores[posMenor]:
            posMenor = i
    return posMenor


def trocar(valores, posX, posY):
    auxiliar = valores[posX]
    valores[posX] = valores[posY]
    valores[posY] = auxiliar
    return None


def preencher(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input("V[" + str(i) + "]: "))
    return None

# ---------------- programa principal -------------- #

N = int(input("Quantidade desejada de elementos: "))
numeros = [0] * N
preencher(numeros)
print(numeros)
ordenar(numeros)
print(numeros)


        
