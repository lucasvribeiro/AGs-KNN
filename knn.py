import sys
import random

# Calcula a Distância Euclidiana dos dois dígitos
def distanciaEuclidiana (linhaTeste, linhaTreina, individuo):
    soma = 0
    i = 0
    while i < 132: #itera por todas as 132 características
        if individuo[i]:
            soma += (linhaTeste[i] - linhaTreina[i]) ** 2 # (x1 - x2)²
        i+=1

    return (soma ** 0.5)            # raiz((x1 - x2)² + (y1 - y2)²)

def kNN (linhaTeste, individuo, treinamento, K):
    classes = [0,0,0,0,0,0,0,0,0,0] # Vetor de classes, cada posição refere-se a uma classe (0-9) onde será armazenado o número de acerto pra mesma
    distancia = []                  # Vetor de distâncias (1000 posições)
    for linhaTreina in treinamento: # Itera por cada um dos 1000 dígitos de treinamento
        distancia.append(distanciaEuclidiana(linhaTeste, linhaTreina, individuo))

    # Descobre qual a classe do dígito que obteve menor distância
    contador = 0        # Contador de K
    while contador < K: # Itera K vezes
        menor = distancia[0]
        pos = 0
        i = 0
        for dist in distancia:
            if dist < menor:
                menor = dist
                pos = i

            i += 1

        classe = int(pos/100)           # Descobre a classe pertencente à menor distância encontrada
        classes[classe] += 1            # Adiciona mais 1 ao vetor de classes, na posição da classe correspondente
        distancia[pos] = float('inf')   # Seta um valor muito alto nessa posição, pois não será mais usada
        contador += 1                   # Adiciona 1 ao contador de K
        
        # zera as variáveis auxiliares e de contador
        menor = distancia[0]
        pos = 0
        i = 0

    maior = max(classes, key=int)   # retorna o maior valor do vetor de classes 
    return classes.index(maior)         # retorna o índice da classe 

def avaliaPopulacao(populacao, teste, treinamento, K):
    populacaoAvaliada = []
    auxDigito = 0
    acertos = 0

    for i in range(7):
        for linhaTeste in teste: # Itera por cada um dos 1000 dígitos de teste
            digito = int(auxDigito/100)
            indice = kNN(linhaTeste, populacao[i], treinamento, K)
            if indice == digito:
                acertos += 1
            auxDigito += 1

        populacaoAvaliada.append((acertos/1000) * 100)
        acertos = 0
        auxDigito = 0
    print("Avaliação da População: ", populacaoAvaliada)
    return populacaoAvaliada

def geraPopulacao(n):
    populacao = []
    individuo = []
    for i in range(n):
        for j in range(132):
            individuo.append(random.randint(0,1))
        populacao.append(individuo)
        individuo = []
    
    return populacao


def recombinacao(populacao, avaliacao):
    pais = []
    piores = []
    piorUm = []
    piorDois = []
    novaPopulacao = []
    novoIndividuo = []

    auxiliar = avaliacao.copy()

    for i in range(2):
        maior = max(avaliacao)
        indiceMaiorAvaliacao = avaliacao.index(maior)
        pais.append(populacao[indiceMaiorAvaliacao])
        if i == 0:
            print("Melhor: ", avaliacao[indiceMaiorAvaliacao])
        avaliacao[indiceMaiorAvaliacao] = -float('inf')
    
    pai = pais[0]
    mae = pais[1]

    for i in range(2):
        menor = min(auxiliar)
        indiceMenorAvaliacao = auxiliar.index(menor)
        piores.append(populacao[indiceMenorAvaliacao])
        print("Pior: ", auxiliar[indiceMenorAvaliacao])
        auxiliar[indiceMenorAvaliacao] = float('inf')
    

    piorUm = piores[0]
    piorDois = piores[1]

    for i in range(2):
        corte = random.randint(1,130)
        novoIndividuo = pai[0:corte] + mae[corte:]
        novaPopulacao.append(novoIndividuo)
    
    for i in range(2):
        corte = random.randint(1,130)
        
        if i == 0:
            novoIndividuo = pai[0:corte] + piorUm[corte:]
        else:
            novoIndividuo = mae[0:corte] + piorDois[corte:]

        novaPopulacao.append(novoIndividuo)
    
    for i in range(2):
        corte = random.randint(1,130)
        novoIndividuo = piorUm[0:corte] + piorDois[corte:]
        novaPopulacao.append(novoIndividuo)
    

    
    novaPopulacao.append(pai)
    
    for i in range(10):
      individuoMutado = random.randint(0,6)
      caracteristicaMutada = random.randint(0,131)

      if(novaPopulacao[individuoMutado][caracteristicaMutada]):
          novaPopulacao[individuoMutado][caracteristicaMutada] = 0
      else:
          novaPopulacao[individuoMutado][caracteristicaMutada] = 1

    return novaPopulacao

def main():
    K = int(sys.argv[1])
    geracao = 1

    # Abrindo arquivos
    arquivoTeste       = open ('teste.txt', 'r')
    arquivoTreinamento = open('treinamento.txt', 'r')

    populacao = geraPopulacao(7) 

    teste = []
    treinamento = []


    linhaTreinamento = arquivoTreinamento.readline()
    while linhaTreinamento:
        arrayFloat = [float(i) for i in linhaTreinamento.rstrip('\n\r').split(' ')]
        treinamento.append(arrayFloat)
        linhaTreinamento = arquivoTreinamento.readline()

    linhaTeste = arquivoTeste.readline()
    while linhaTeste:
        arrayFloat = [float(i) for i in linhaTeste.rstrip('\n\r').split(' ')]
        teste.append(arrayFloat)
        linhaTeste = arquivoTeste.readline()

    while True:
        print("* GERAÇÃO ", geracao , " *")
        avaliacao = avaliaPopulacao(populacao, teste, treinamento, K)
        novaPopulacao = recombinacao(populacao, avaliacao)
        populacao = novaPopulacao
        geracao += 1
        print("-------------------------------------------")
main()