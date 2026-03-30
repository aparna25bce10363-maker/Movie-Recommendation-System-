import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("movies.csv")

# Convert genre into numerical form
vectorizer = TfidfVectorizer()

print(data.columns)
tfidf_matrix = vectorizer.fit_transform(data['genre'])

# Compute similarity
similarity = cosine_similarity(tfidf_matrix)

# Function to recommend movies
def recommend(movie_name):
    movie_name = movie_name.lower()
    
    # Find index of movie
    indices = data[data['title'].str.lower() == movie_name].index
    
    if len(indices) == 0:
        return ["Movie not found"]
    
    idx = indices[0]
    
    # Get similarity scores
    scores = list(enumerate(similarity[idx]))
    
    # Sort movies based on similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Get top 5 recommendations
    recommendations = []
    for i in scores[1:6]:
        recommendations.append(data.iloc[i[0]]['title'])
    
    return recommendations
