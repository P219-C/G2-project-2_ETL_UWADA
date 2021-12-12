#Dependencies
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

#Importing Spotify client_ID and secret_code
from keys import client_id, client_secret

#scrapped_date
from datetime import datetime

def search(table):
    #running spotipy search function
    results = sp.search(q='track:' + table['song_title'], type = 'track')
    tracks = results ['tracks']['items']
    if len(tracks) == 0:
        raise Exception('Song details not found') 
    #extracting spotify ID for the track **Important to make further API calls**
    table['track_spotify ID'] = tracks[0]['id']
    table['artist_spotify ID'] = tracks[0]['album']['artists'][0]['id']

    #song_table: song_duration,release_date

    try:
        table['song_duration[ms]'] = tracks[0]['duration_ms']
    except:
        table['song_duration[ms]'] = ""

    try:
        table['release_date'] = tracks[0]['album']['release_date']
    except:
        table['release_date'] = ""

    try:
        table['popularity'] = tracks[0]['popularity']  
    except:
        table['popularity'] = ""

    # genre_table: genre
    try:
        table['song_genre'] = tracks[0]['genre']
    except:
        table['song_genre'] = ""

    # album_table: album_name, album_type 
    try:
        table['album_name'] = tracks[0]['album']['name']
    except:
        table['album_name'] = ""
    try:
        table['album_type'] = tracks[0]['album']['album_type']
    except:
        table['album_type'] = ""

    return table