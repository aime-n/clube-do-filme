#%%
import pandas as pd
from imdb import IMDb
# Função para obter a duração de um filme
def obter_duracao(filme):
    try:
        resultado = ia.search_movie(filme)
        if resultado:
            filme_info = resultado[0]
            ia.update(filme_info)
            return filme_info.get('runtimes', ['Desconhecido'])[0]
        else:
            return 'Desconhecido'
    except:
        return 'Desconhecido'
    

def obter_ano(filme):
    try:
        # Buscando o filme pelo nome
        resultado = ia.search_movie(filme)
        if resultado:
            # Pegando o primeiro resultado
            filme_info = resultado[0]
            ia.update(filme_info)
            # Obtendo o ano do filme
            ano = filme_info.get('year', 'Desconhecido')
            print(filme, ano)
            return ano
        else:
            return 'Desconhecido'
    except Exception as e:
        # Em caso de erro, retorna 'Desconhecido' (e loga o erro para depuração)
        print(f"Erro: {e}")
        return 'Desconhecido'

import os
import requests
from bs4 import BeautifulSoup

# Função para obter a URL da capa de um filme
def obter_url_capa(nome_do_filme):
    try:
        # Buscando o filme pelo nome
        resultados = ia.search_movie(nome_do_filme)
        if resultados:
            # Pegando o primeiro resultado (mais provável que seja o filme correto)
            filme = resultados[0]
            # Obtendo o ID do filme
            id_filme = filme.movieID
            # Obtendo informações do filme usando o ID
            filme_info = ia.get_movie(id_filme)
            # Retornando a URL da capa do filme
            url = filme_info.get('cover url', 'Desconhecido')
            print(url)
            return url
        else:
            return 'Desconhecido'
    except Exception as e:
        # Retornando 'Desconhecido' em caso de erro (e logando o erro para depuração)
        print(f"Erro: {e}")
        return 'Desconhecido'
    
import requests

def salvar_capa(filme, url):
    try:
        if url != 'Desconhecido':
            response = requests.get(url)
            if response.status_code == 200:
                # nome_arquivo = f"capas_filmes/{filme['Nome do Filme']}.jpg"
                nome_arquivo = f"capas_filmes/{filme['Nome do Filme']} ({filme['Ano']}).jpg"
                with open(nome_arquivo, 'wb') as file:
                    file.write(response.content)
                print('capa salva')
                return nome_arquivo
        return 'Desconhecido'
    except Exception as e:
        print(f"Erro: {e}")
        return 'Desconhecido'




#%%
# Ler a planilha e instanciar IMDb
planilha = pd.read_csv('filmes - guily pleasure.csv') 
# planilha.rename(columns={0: 'Nome do Filme'}, inplace=True)

# Criar uma instância do IMDb
ia = IMDb()


#%%
# Aplicar a função para obter a duração a cada filme na planilha
planilha['Duração'] = planilha['Nome do Filme'].apply(obter_duracao)

#%%
planilha['Ano'] = planilha['Nome do Filme'].apply(obter_ano)


#%%
planilha = planilha[planilha['Duração'] <= 100]

# Salvar a planilha com a nova coluna

# %%



# Aplicar a função para obter a URL da capa a cada filme na planilha
planilha['URL da Capa'] = planilha['Nome do Filme'].apply(obter_url_capa)

# %%

# Criar uma pasta para salvar as capas
if not os.path.exists('capas_filmes'):
    os.makedirs('capas_filmes')

# Aplicar a função para salvar a capa de cada filme na planilha
planilha['Arquivo da Capa'] = planilha.apply(lambda row: salvar_capa(row, row['URL da Capa']), axis=1)
# %%
# Salvar a planilha com os nomes dos arquivos das capas
planilha.to_csv('nomes_filmes_com_capas.xlsx', index=False)  # Substitua pelo nome do arquivo de saída desejado
