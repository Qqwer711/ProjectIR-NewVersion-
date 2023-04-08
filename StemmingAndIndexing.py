import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
import pandas as pd



import re
from nltk.stem import PorterStemmer

with open('article_titles_fixing.txt', 'r') as f:
    text = f.read()

text = re.sub(r'[^a-zA-Z\s]', '', text)


words = text.split()


stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_text = ' '.join(stemmed_words)

with open('article_titles_stemmed.txt', 'w') as f:
    f.write(stemmed_text)



with open('article_titles_stemmed.txt', 'r') as f:
    text = f.read()


vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform([text])

feature_names = vectorizer.get_feature_names()


for i, feature in enumerate(feature_names):
    weight = tfidf_matrix[0, i]
    print(f"{feature}: {weight:.5f}")


df = pd.DataFrame({'feature': feature_names, 'weight': tfidf_matrix.toarray()[0]})
df.to_csv('weights.csv', index=False)
