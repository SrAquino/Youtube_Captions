import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import sys
import os
# Adiciona a pasta raiz ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Função de normalização
def normalize_text(text):
    # Converter para letras minúsculas
    text = text.lower()
    # Remover pontuações e caracteres especiais
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenizar (dividir o texto em palavras)
    words = word_tokenize(text)
    # Remover stopwords (em português, mas pode mudar para inglês)
    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in words if word not in stop_words]
    # Lematizar (reduzir às formas básicas)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Recriar o texto normalizado
    normalized_text = ' '.join(words)
    return normalized_text

def get_stopwords_for_language(language_code):
    # Pegar a parte inicial do idioma (e.g., 'en' de 'en-US')
    lang = language_code.split('-')[0]
    try:
        #return set(stopwords.words(lang))
        print(f'tudo ok com {lang}')
    except OSError:
        print(f"Stop words para o idioma '{lang}' não estão disponíveis.")
        #return set()  # Retorna conjunto vazio caso o idioma não esteja disponível

'''
# Exemplo de uso
example_text = "A Ciência e a Tecnologia estão mudando o mundo, mas é importante entender as suas limitações."
normalized = normalize_text(example_text)
print("Texto Original:", example_text)
print("Texto Normalizado:", normalized)
'''

from Funcs.db import get_unique_languages

uniq = get_unique_languages('videos_data.db','links')
for u in uniq:
    print(u)
    get_stopwords_for_language(u)