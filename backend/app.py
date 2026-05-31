from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from movie_engine import recommender

app = Flask(__name__)
CORS(app)

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    limit = int(request.args.get('limit', 10))
    if not query:
        return jsonify([])
    results = recommender.search(query, limit)
    return jsonify(results)

@app.route('/api/recommend/<int:movie_id>')
def recommend(movie_id):
    n = int(request.args.get('n', 8))
    results = recommender.get_recommendations(movie_id, n)
    return jsonify(results)

@app.route('/api/movie/<int:movie_id>')
def get_movie(movie_id):
    movie = recommender.get_movie_by_id(movie_id)
    if not movie:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(movie)

@app.route('/api/top-rated')
def top_rated():
    n = int(request.args.get('n', 10))
    results = recommender.get_top_rated(n)
    return jsonify(results)

@app.route('/api/genre/<genre>')
def by_genre(genre):
    n = int(request.args.get('n', 8))
    results = recommender.get_genre_recommendations(genre, n)
    return jsonify(results)

@app.route('/api/genres')
def genres():
    return jsonify(recommender.get_all_genres())

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'movies': len(recommender.df)})

if __name__ == '__main__':
    print("Starting Movie Recommendation API on port 5000...")
    app.run(debug=False, host='0.0.0.0', port=5000)