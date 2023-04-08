from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

nltk.download('punkt')


with open('article_titles_fixing.txt', 'r') as f:
    articles = f.readlines()

stemmer = PorterStemmer()
stemmed_articles = [' '.join([stemmer.stem(word) for word in article.split()]) for article in articles]


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(stemmed_articles)



query = input("Enter query : ")
query_vector = vectorizer.transform([query])
similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

score_df = pd.DataFrame({'document': range(1, len(articles)+1), 
                         'similarity_score': similarity_scores[0], 
                         'stemmed_text': stemmed_articles})


score_df.to_csv('similarity_scores.csv', index=False)

for i in score_df.sort_values(by=['similarity_score'], ascending=False)['document']:
    print(f"Document {i}: {score_df[score_df['document']==i]['similarity_score'].values[0]:.5f}")

