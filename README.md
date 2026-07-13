# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit. This application recommends similar movies based on the movie selected by the user and displays their posters using the TMDB API.

---

## 🚀 Features

- Recommend movies based on content similarity
- Displays movie posters
- Fast and interactive Streamlit web interface
- Uses cosine similarity for recommendations
- Clean and user-friendly interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- Pickle
- TMDB API

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│── app.py
│── Movie Recommendation.ipynb
│── movies.pkl
│── similarity.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** containing movie information such as:

- Movie Title
- Cast
- Crew
- Genres
- Keywords
- Overview

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### Move into the project folder

```bash
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Loads movie data.
2. Preprocesses movie metadata.
3. Creates tags using genres, keywords, cast, crew, and overview.
4. Converts text into vectors using CountVectorizer.
5. Calculates cosine similarity between movies.
6. Recommends the top 5 most similar movies.
7. Fetches movie posters using the TMDB API.

---

## 📸 Screenshots

Add screenshots of your application here after uploading them to the repository.

Example:

```
images/home.png
```

---

## 📌 Future Improvements

- Hybrid recommendation system
- User authentication
- Search suggestions
- Movie ratings and reviews
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

**Arpan Singh**

GitHub: https://github.com/your-username

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
