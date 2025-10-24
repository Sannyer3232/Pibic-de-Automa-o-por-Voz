# modulo_interpretacao.py
# Responsável pelo PLN: pré-processamento e identificação da intenção.

import nltk
import joblib # Importa o joblib para salvar/carregar o modelo
import os
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config import intents

# Define o caminho para o modelo salvo
MODELO_PATH = "tfidf_vectorizer.joblib"

# Garante que os pacotes NLTK necessários estão baixados
def baixar_dependencias_nltk():
    """
    Verifica se os pacotes NLTK estão instalados e baixa APENAS se necessário.
    """
    print("Verificando dependências NLTK...")
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('stammers/rslp')
        print("Dependências NLTK já estão satisfeitas.")
    except LookupError:
        print("Baixando dependências NLTK (punkt, stopwords, rslp)... Isso só acontece uma vez.")
        nltk.download("punkt", quiet=True)
        nltk.download("stopwords", quiet=True)
        nltk.download("rslp", quiet=True)
        print("Dependências NLTK baixadas com sucesso.")

# --- Funções de Pré-processamento ---

def preprocessar(frase):
    """
    Limpa e processa uma única frase (tokeniza, remove stopwords, aplica stemming).
    """
    stop_words = set(stopwords.words("portuguese"))
    stemmer = RSLPStemmer()
    tokens = word_tokenize(frase.lower())
    tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(tokens)

# --- Funções do Modelo TF-IDF ---

def obter_ou_criar_vectorizer():
    """
    Carrega o modelo TF-IDF de um arquivo, se existir.
    Se não, cria, treina e salva um novo modelo.
    """
    baixar_dependencias_nltk() # Primeiro, verifica os pacotes NLTK
    
    try:
        # Tenta carregar o modelo que já foi treinado
        vectorizer = joblib.load(MODELO_PATH)
        print(f"Modelo TF-IDF carregado com sucesso de '{MODELO_PATH}'.")
    except FileNotFoundError:
        # Se o arquivo não existe, cria um novo
        print(f"Arquivo '{MODELO_PATH}' não encontrado. Criando e treinando um novo modelo...")
        
        vectorizer = TfidfVectorizer()
        # Cria o dataset de treinamento a partir das chaves do dicionário 'intents'
        dataset = [preprocessar(frase) for frases in intents.values() for frase in frases]
        
        # Treina (fit) o modelo
        vectorizer.fit(dataset)
        print("Novo modelo TF-IDF treinado.")
        
        # Salva o modelo treinado no arquivo
        joblib.dump(vectorizer, MODELO_PATH)
        print(f"Modelo salvo em '{MODELO_PATH}' para uso futuro.")
    
    return vectorizer

def identificar_intencao(comando, vectorizer, limiar=0.5):
    """
    Compara o comando do usuário com o modelo TF-IDF e encontra a intenção mais provável.
    """
    comando_proc = preprocessar(comando)
    comando_vec = vectorizer.transform([comando_proc])
    
    melhor_intencao = None
    melhor_similaridade = 0
    
    for intencao, frases in intents.items():
        # Transforma as frases da intenção atual
        frases_vec = vectorizer.transform([preprocessar(frase) for frase in frases])
        # Calcula a similaridade do cosseno
        similaridades = cosine_similarity(comando_vec, frases_vec)
        # Pega a maior similaridade entre o comando e as frases desta intenção
        max_sim = np.max(similaridades)
        
        if max_sim > melhor_similaridade:
            melhor_similaridade = max_sim
            melhor_intencao = intencao
    
    # Retorna a intenção apenas se for maior que o limiar de confiança
    return melhor_intencao if melhor_similaridade > limiar else None