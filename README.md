# 🎬 CineMatch — AI Movie Recommendation System

> A machine learning-powered movie recommendation system with content-based filtering, cosine similarity, and a cinematic dark-themed web interface.

---

## 📌 Objective

Help users discover movies they'll love by analyzing film metadata — genres, directors, cast, plot — using TF-IDF vectorization and cosine similarity to surface personalized recommendations. Built as a full-stack ML application with a live REST API and interactive frontend.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🔍 Smart Search | Real-time search by title, genre, director, or actor |
| 🤖 Content-Based Filtering | TF-IDF + Cosine Similarity across 150 curated films |
| 📊 Similarity Scores | Each recommendation shows a % match score |
| 🎭 Genre Browsing | Filter films by 13 genre categories |
| ⭐ Top Rated | Discover the highest-rated films instantly |
| 🎥 Movie Detail View | Plot, cast, director, runtime, votes, rating |
| 📱 Responsive UI | Works on desktop and mobile |
| 🌐 REST API | Clean Flask API with 6 endpoints |

---

## 🧠 Machine Learning Pipeline

```
Raw Movie Data (150 films)
        ↓
Feature Engineering
  └─ Combine: genres + director + cast + plot → "tags" column
        ↓
TF-IDF Vectorization (5000 features, English stop words removed)
        ↓
Cosine Similarity Matrix (150 × 150)
        ↓
Recommendation Engine
  └─ Given movie_id → rank by similarity score → return top N
```

### Algorithms Used
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Converts movie metadata text into weighted numerical vectors
- **Cosine Similarity**: Measures the angular similarity between movie vectors in high-dimensional space
- **Content-Based Filtering**: Recommends movies similar in style, genre, director, cast to the selected film
- **MinMaxScaler**: Used for normalizing rating/vote features

---

## 🗂️ Tech Stack

| Layer | Technology |
|---|---|
| ML Engine | scikit-learn, pandas, numpy |
| Backend API | Python 3, Flask, Flask-CORS |
| Frontend | Vanilla HTML/CSS/JS |
| Fonts | Google Fonts (DM Serif Display, DM Sans) |
| Data | Custom curated dataset (150 films, IMDb-based) |

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cinematch-recommender.git
cd cinematch-recommender
```

### 2. Install dependencies
```bash
pip install flask flask-cors scikit-learn pandas numpy requests
```

### 3. Start the backend API
```bash
cd backend
python app.py
```
The API will run at `http://localhost:5000`

### 4. Open the frontend
Open `frontend/index.html` in your browser (or serve with any static server):
```bash
# Option A: Python simple server
cd frontend
python -m http.server 8080

# Option B: Open directly
open frontend/index.html
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Health check, returns movie count |
| GET | `/api/search?q={query}` | Search movies by title/genre/director/cast |
| GET | `/api/movie/{id}` | Get single movie details |
| GET | `/api/recommend/{id}?n=8` | Get N content-based recommendations |
| GET | `/api/top-rated?n=10` | Get top N movies by rating |
| GET | `/api/genre/{genre}?n=8` | Get top N movies in a genre |

### Example API Calls
```bash
# Search for Nolan films
curl "http://localhost:5000/api/search?q=nolan"

# Get recommendations for The Dark Knight (id=3)
curl "http://localhost:5000/api/recommend/3?n=6"

# Get top 5 rated films
curl "http://localhost:5000/api/top-rated?n=5"

# Browse Sci-Fi films
curl "http://localhost:5000/api/genre/Sci-Fi"
```

---

## 📁 Project Structure

```
cinematch-recommender/
├── backend/
│   ├── app.py              # Flask REST API (6 endpoints)
│   └── movie_engine.py     # ML engine: dataset + TF-IDF + cosine similarity
├── frontend/
│   └── index.html          # Full single-page application (cinematic dark UI)
├── README.md
└── requirements.txt
```

---

## 🧪 How Recommendations Work

When you click on a movie (e.g., *Inception*):

1. The system finds its index in the TF-IDF matrix
2. Computes cosine similarity against all 150 other films
3. Ranks by similarity score (0–100%)
4. Returns the top 8 most similar films
5. Similarity scores are displayed as progress bars in the UI

**Why these movies are similar:**
- Same director → very high weight (Christopher Nolan films cluster together)
- Same genres → high weight
- Overlapping cast → medium weight
- Similar plot keywords → medium weight

---

## 📊 Dataset

- **150 curated films** spanning 1942–2024
- Fields: `id`, `title`, `year`, `genres`, `director`, `cast`, `plot`, `rating`, `votes`, `runtime`, `language`
- Sourced from IMDb top-rated lists, curated manually for diversity
- Covers genres: Drama, Action, Comedy, Crime, Sci-Fi, Horror, Romance, Thriller, Fantasy, Animation, War, Mystery, Western, Biography, Music, Sport

---

## 🔮 Future Enhancements

- [ ] **Collaborative Filtering** — user-based ratings matrix (SVD/ALS)
- [ ] **Hybrid Recommender** — combine content + collaborative signals
- [ ] **User accounts** — persist watch history and ratings
- [ ] **TMDb API integration** — real poster images and full metadata
- [ ] **Deployed version** — host on Render / Railway / Vercel

---

## 👨‍💻 Author

Built for the ML Domain — Round 2 Assignment  
Submitted: May 2026
