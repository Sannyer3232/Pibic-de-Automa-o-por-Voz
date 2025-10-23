# modulo_interpretacao.py
# Responsável pelo PLN: pré-processamento e identificação da intenção.

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Importa a base de conhecimento
from config import intents

# Garante que os pacotes NLTK necessários estão baixados
def baixar_dependencias_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('stammers/rslp')
    except LookupError:
        print("Baixando dependências NLTK (punkt, stopwords, rslp)...")
        nltk.download("punkt", quiet=True)
        nltk.download("stopwords", quiet=True)
        nltk.download("rslp", quiet=True)

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

def inicializar_vectorizer():
    """
    Cria e "treina" o modelo TF-IDF com base nas intenções do config.py.
    Retorna o vectorizer treinado.
    """
    print("Inicializando e treinando o modelo TF-IDF...")
    baixar_dependencias_nltk()
    vectorizer = TfidfVectorizer()
    # Cria o dataset de treinamento a partir das chaves do dicionário 'intents'
    dataset = [preprocessar(frase) for frases in intents.values() for frase in frases]
    vectorizer.fit(dataset)
    print("Modelo TF-IDF pronto.")
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