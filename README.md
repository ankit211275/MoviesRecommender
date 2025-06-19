# MoviesRecommender

Welcome to the Movie Recommender System! This project builds a personalized recommendation engine using content-based filtering on the TMDB 5000 Movie Dataset. You can try it out live here:

🔗 Live Demo: moviesrecommender-xqt6.onrender.com

⸻
## 🧠 Project Overview

This system recommends movies similar to the one you select based on:
	•	Genres
	•	Overview
	•	Keywords
	•	Cast
	•	Crew

Using natural language processing (NLP) techniques and a vector similarity approach (cosine similarity), it identifies and ranks the most relevant movies.

## 📌 Features
	•	✅ Cleaned and preprocessed movie metadata
	•	✅ NLP vectorization of movie tags
	•	✅ Cosine similarity-based recommendations
	•	✅ Interactive UI built with Streamlit
	•	✅ Fast and lightweight (using .pkl model file)

## 🛠 How It Works
	1.	Data Loading:
	•	Datasets used: tmdb_5000_movies.csv, tmdb_5000_credits.csv
	2.	Preprocessing:
	•	Merges the datasets on movie titles
	•	Extracts relevant features: genres, keywords, cast, crew, overview
	•	Converts text columns from JSON-like strings to Python lists using ast.literal_eval
	•	Combines all relevant textual data into a single tags field
	3.	Vectorization:
	•	Uses CountVectorizer from sklearn to convert text into numerical vectors
	•	Computes pairwise cosine similarity matrix for all movies
	4.	Recommendation:
	•	For any selected movie, the top 5 most similar movies (based on vector distance) are returned
	5.	Deployment:
	•	App built with Streamlit and deployed on Render

⸻

## 💡 Example

🔍 Input: “The Dark Knight”
🎬 Recommended:
	•	Batman Begins
	•	The Prestige
	•	Man of Steel
	•	The Avengers
	•	Iron Man

⸻

## 📁 Project Structure

📦MovieRecommender
 ┣ app.py
 ┣ MoviesRecommenderSystems.ipynb
 ┣ tmdb_5000_movies.csv
 ┣ tmdb_5000_credits.csv
 ┣ similarity.pkl
 ┣ movies.pkl
 ┗ README.md

 ## 🚀 Running the App Locally

1. Clone the repo
git clone https://github.com/yourusername/MovieRecommender.git
cd MovieRecommender
2. Create & activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install requirements
pip install -r requirements.txt
4. Run Streamlit app
streamlit run app.py

## 📦 Dataset
	•	Source: TMDB 5000 Movie Dataset on Kaggle
	•	Files used:
	•	tmdb_5000_movies.csv
	•	tmdb_5000_credits.csv

## 🧪 Performance & Success

This content-based movie recommendation engine provides relevant and engaging suggestions based on user input. It is:
	•	🎯 Accurate at identifying similar genres, themes, and cast-related content
	•	⚡ Fast and efficient (runs locally and online with minimal latency)
	•	🧠 Doesn’t require user history — great for cold-start scenarios

✅ Real-world use case: This app has been actively used and appreciated by 100+ of my classmates, hostelmates, and friends, who found the recommendations surprisingly spot-on for exploring new movies similar to their favorites.

To explore its performance for yourself, just try the live demo and enter any movie you love!

## 🔗 Launch the app