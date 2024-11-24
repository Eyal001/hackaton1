import requests
import pygame
import base64
from io import BytesIO
import os
from dotenv import load_dotenv
import threading

# Spotify API: Get Token
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

# Search Spotify and Get Track Preview URL
def search_spotify_and_get_preview(token, query):
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json()["tracks"]["items"]
        # print('tracks :' ,tracks)
        if tracks:
            track = tracks[0]
            track_name = track["name"]
            artist_name = track["artists"][0]["name"]
            preview_url = track["preview_url"]

            # print(f"Playing: {track_name} by {artist_name}")
            return preview_url
        else:
            print("No tracks found for the given query.")
            return None
    else:
        print("Error fetching data from Spotify:", response.json())
        return None

# Play Preview from URL Using pygame
def play_from_url(url):
    if not url:
        print("No preview available for this track.")
        return

    # print("Playing the preview...")
    response = requests.get(url)
    audio_data = BytesIO(response.content)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_data, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass




def play_sound(type, stop_event):
        
    load_dotenv()
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')    

    token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)

    
    query = f"{type} relaxing sound"
    preview_url = search_spotify_and_get_preview(token, query)

    # Play the Preview
    while not stop_event.is_set():
        play_from_url(preview_url)
    
    
