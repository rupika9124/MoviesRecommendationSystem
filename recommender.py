import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your movie dataset
movies_data = pd.read_csv('movies.csv')

# Create a 'combined' column for TF-IDF vectorization based on available columns
movies_data['combined'] = movies_data['overview'].fillna('') + ' ' + \
                          movies_data['genres'].fillna('') + ' ' + \
                          movies_data['tagline'].fillna('')

# Preprocess and vectorize movie data
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_data['combined'])

# Compute the cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)
