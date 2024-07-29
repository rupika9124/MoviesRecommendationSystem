import streamlit as st
import pandas as pd
import difflib
from recommender import movies_data, similarity

def recommend_movies(movie_name, movies_data, similarity):
    close_matches = difflib.get_close_matches(movie_name, movies_data['title'].tolist(), n=1)
    close_match = close_matches[0] if close_matches else None

    if close_match:
        index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        recommended_movies = []
        max_suggestions = 20
        for i, movie in enumerate(sorted_similar_movies, start=1):
            index = movie[0]
            title_from_index = movies_data.loc[index, 'title']
            if title_from_index != close_match:
                recommended_movies.append(title_from_index)
                if i == max_suggestions:
                    break
        return close_match, recommended_movies
    else:
        return None, []

st.title("Movie Recommendation System")

movie_name = st.text_input('Enter your favorite movie name:')
if st.button("Recommend"):
    if movie_name:
        close_match, recommended_movies = recommend_movies(movie_name, movies_data, similarity)
        if close_match:
            st.write(f'Movies suggested for you based on "{close_match}":')
            for i, movie in enumerate(recommended_movies, start=1):
                st.write(f"{i}. {movie}")
        else:
            st.write(f'No recommendations found for "{movie_name}".')
    else:
        st.write("Please enter a movie name to get recommendations.")
