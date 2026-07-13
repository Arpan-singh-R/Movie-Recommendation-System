import streamlit as st
import pickle


# Load saved files
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


# Movie names
movie_list = movies['title'].values


# Streamlit UI
st.title("🎬 Movie Recommendation System")


selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)


if st.button("Recommend"):

    movie_index = movies[
        movies['title'] == selected_movie
    ].index[0]


    distances = similarity[movie_index]


    recommendations = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]


    st.subheader("Recommended Movies")


    for i in recommendations:

        st.write(
            "🎥",
            movies.iloc[i[0]].title
        )
        