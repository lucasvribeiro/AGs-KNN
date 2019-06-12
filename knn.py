# Abrindo arquivos
teste       = open ('teste.txt', 'r')
treinamento = open('treinamento.txt', 'r')

# Separando por linhas
teste       = teste.readlines()
treinamento = treinamento.readlines()

def algoritmo (linhaTeste, linhaTreina):
    soma = 0
    i = 0
    while i < 132: #itera por todas as 132 características
        soma += ((float(linhaTeste[i]) - float(linhaTreina[i])) ** 2) # (x1 - x2)²
        i+=1

    return (soma ** 0.5) # raiz((x1 - x2)² + (y1 - y2)²)

def comparaLinha (linhaTeste):
    diferenca = []
    for linhaTreina in treinamento: # Itera por cada um dos 1000 dígitos de treinamento
        linhaTreina = linhaTreina.split(' ')
        diferenca.append(algoritmo(linhaTeste, linhaTreina))

    print(diferenca) # Printa um vetor de diferença pra cada dígito de teste

for linhaTeste in teste: # Itera por cada um dos 1000 dígitos de teste
    linhaTeste = linhaTeste.split(' ')
    comparaLinha(linhaTeste)
