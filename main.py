import pandas as pd
import random

# Abrir o arquivo para leitura
with open('filmes.txt', 'r', encoding='utf-8') as arquivo:
    # Ler todas as linhas e remover a quebra de linha de cada uma
    lista = [linha.strip() for linha in arquivo]

# Definindo a seed
random.seed(888)

# Sorteando 4 valores da lista
sorteados = random.sample(lista, 4)

# Imprimindo os valores sorteados
print(sorteados)

