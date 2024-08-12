import streamlit as st
import joblib
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("http://api.themoviedb.org/3/movie/{}?api_key=9fe290105a90e875898bebb187c82dbb&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']
# Recommend function
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_indices:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


# Load the movies data and similarity matrix
movies_list = joblib.load('movies.pkl')
movies_list = pd.DataFrame(movies_list)
similarity = joblib.load('similarity.pkl')

# Streamlit app
st.title("Movies Recommender System")
selected_movie_name = st.selectbox('Select a movie', movies_list['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    st.write("Recommended Movies:")
    # display posters
    columns = st.columns(5)

    for i in range(5):

        with columns[i]:
            st.text(names[i])
            st.image(posters[i])
    st.success('Found!', icon="✅")