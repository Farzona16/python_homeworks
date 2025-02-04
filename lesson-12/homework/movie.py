import requests
import random

api_key = "f33f605d" 
url = "http://www.omdbapi.com/"

def get_movie_by_genre(genre):
    params = {
        "apikey": api_key,
        "s": genre,  
        "type": "movie"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        if "Search" in data:
            movies = data["Search"]
            random_movie = random.choice(movies)
            return random_movie["Title"]
        
        else:
            print("Not found any film")
            return None
    else:
        print(f"Error occurred: {response.status_code}")
        return None

def get_movie_details(title):
    params = {
        "apikey": api_key,
        "t": title
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error occurred: {response.status_code}")
        return None

genre = input("Enter the genre of film (For example: Action, Comedy, Horror): ")

random_movie_title = get_movie_by_genre(genre)

if random_movie_title:
    movie_data = get_movie_details(random_movie_title)
    
    if movie_data:
        print(f" Title : {movie_data['Title']}")
        print(f"Genre: {movie_data['Genre']}")
    else:
        print("Error occurred")
else:
    print("There is no film in this genre")
