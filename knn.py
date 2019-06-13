# Abrindo arquivos
teste       = open ('teste.txt', 'r')
treinamento = open('treinamento.txt', 'r')

# Separando por linhas
teste       = teste.readlines()
treinamento = treinamento.readlines()

# Calcula a Distância Euclidiana dos dois dígitos
def algoritmo (linhaTeste, linhaTreina):
    soma = 0
    i = 0
    while i < 132: #itera por todas as 132 características
        soma += ((float(linhaTeste[i]) - float(linhaTreina[i])) ** 2) # (x1 - x2)²
        i+=1

    return (soma ** 0.5)            # raiz((x1 - x2)² + (y1 - y2)²)
    
def comparaLinha (linhaTeste):
    classes = [0,0,0,0,0,0,0,0,0,0] # Vetor de classes, cada posição refere-se a uma classe (0-9) onde será armazenado o número de acerto pra mesma
    distancia = []                  # Vetor de distâncias (1000 posições)
    for linhaTreina in treinamento: # Itera por cada um dos 1000 dígitos de treinamento
        linhaTreina = linhaTreina.split(' ')
        distancia.append(algoritmo(linhaTeste, linhaTreina))

    # Descobre qual a classe do dígito que obteve menor distância
    contador = 0        # Contador de K
    while contador < 9: # Itera K vezes
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

    print(classes)       #retorna o vetor de classes

for linhaTeste in teste: # Itera por cada um dos 1000 dígitos de teste
    linhaTeste = linhaTeste.split(' ')
    comparaLinha(linhaTeste)
