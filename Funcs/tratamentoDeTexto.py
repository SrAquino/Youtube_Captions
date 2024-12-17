import nltk
from nltk.data import find
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def ensure_nltk_resource(resource_name):
    try:
        # Tenta localizar o recurso
        find(resource_name)
        print(f"Recurso '{resource_name}' já está disponível.")
    except LookupError:
        print(f"Recurso '{resource_name}' não encontrado. Fazendo o download...")
        nltk.download(resource_name)

# Verifica e baixa os recursos necessários
ensure_nltk_resource('tokenizers/punkt')
ensure_nltk_resource('corpora/stopwords.zip')
ensure_nltk_resource('corpora/wordnet.zip')

def get_stopwords_for_language(language_code):
    # Pegar a parte inicial do idioma (e.g., 'en' de 'en-US')
    lang = language_code.split('-')[0]

    mapping = {
        'en-US': 'english',
        'en': 'english',
        'en-GB': 'english',
        'hi': 'hindi',
        'en-IN': 'english',
        'ar': 'arabic',
        'ta': 'tamil',
        'pt': 'portuguese',
        'pt-BR': 'portuguese',
    }

    try:
        return set(stopwords.words(mapping.get(language_code, None)))
    except OSError:
        print(f"Stop words para o idioma '{lang}' não estão disponíveis.")
        return set()  # Retorna conjunto vazio caso o idioma não esteja disponível

def remove_stopwords(text, language_code):
    stop_words = get_stopwords_for_language(language_code)
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def normalize_text(text, language_code):
    # Remover pontuações e caracteres especiais
    text = re.sub(r'[^\w\s]', '', text)

    # Remover stopwords
    words = remove_stopwords(text, language_code)
    
    # Tokenizar (dividir o texto em palavras)
    words = word_tokenize(words)

    # Lematizar (reduzir às formas básicas)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Recriar o texto normalizado
    normalized_text = ' '.join(words)

    #print(normalized_text)
    return normalized_text
