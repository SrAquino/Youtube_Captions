import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Exemplo de textos normalizados (substitua pelos seus textos)
textos = [
    "O gato está na janela",
    "O cachorro está no jardim",
    "A janela está aberta"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(textos)  # Vetoriza os textos

print("Matriz TF-IDF:")
print(tfidf_matrix.toarray())  # Converte a matriz esparsa para densa
print("Palavras mapeadas:")
print(vectorizer.get_feature_names_out())  # Palavras que compõem o vocabulário

