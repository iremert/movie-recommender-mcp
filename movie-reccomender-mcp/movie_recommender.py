import requests
import os

API_KEY = os.getenv("c6fae702c36224d5f01778d394772520", "demo")  # Gerçek API key ile değiştir

def get_movie_recommendation(keyword):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={keyword}"
    response = requests.get(url)
    data = response.json()

    if "results" not in data or not data["results"]:
        return "Hiç film bulunamadı."

    movie = data["results"][0]
    title = movie.get("title", "Bilinmiyor")
    overview = movie.get("overview", "Açıklama yok.")
    release_date = movie.get("release_date", "Tarih yok")

    return f"🎬 Önerilen Film: {title} ({release_date})\n\n{overview}"
