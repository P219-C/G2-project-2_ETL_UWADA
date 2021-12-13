# Billboard Hot 100
## Import Dependencies 
#Importing dependencies for web scrapping
from bs4 import BeautifulSoup
import requests
import pandas as pd

## Web Scrapping -  Hot 100
import web_scraping
# running the web scrapping function
top_100_scrapped_df = web_scraping()
# Spotify Data Search
## Spotify for Developers - Using Spotify Library 
"""
Link to spotipy library docs
https://spotipy.readthedocs.io/en/2.19.0/#

"""

#Dependencies
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np

#Importing Spotify client_ID and secret_code
from keys import client_id, client_secret
#adding empty columns to the 'top_100_scrapped_df' to indicate search info
top_100_scrapped_df['track_spotify_ID']=""
top_100_scrapped_df['artist_spotify_ID']=""
top_100_scrapped_df['song_duration[ms]']=""
top_100_scrapped_df['song_release_date']=""
top_100_scrapped_df['spotify_popularity']=""
top_100_scrapped_df['album_name'] =""
top_100_scrapped_df['album_type']=""

#Displaying main table
top_100_scrapped_df

#Authenticating requests using Client Credential Flow
scope = "user-library-read"
sp = sp.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
## Search function - Extracting song, artist and album data from Spotify
# function to extract data for any track using search
# Note: The function below extracts song_title from the a table with column_header called 'song_title'

import search_function
# Iterating search function for each row of the top_100_scrapped_df 
for index,row in top_100_scrapped_df.iterrows():
    top_100_scrapped_df.loc[index,:] = search(row)

# creating output csv for main table
top_100_scrapped_df.to_csv('Output_CSV/top_100_scrapped_df.csv', index=False)

# displaying top_100_scrapped_df 
top_100_scrapped_df
# dropping songs for failed searchs
nan_value = float("NaN")
top_100_cleaned_df = top_100_scrapped_df.replace("", nan_value)
top_100_cleaned_df = top_100_cleaned_df.dropna(subset = ["track_spotify_ID"])

print(f'\nSongs with no search results have been dropped.\nDataFrame contains {len(top_100_cleaned_df)} rows')

top_100_cleaned_df
## Creating DataFrames - song_df, artist_df, album_df, concert_df
### Inspecting and cleaning the collected data
# ERD Diagram for reference
# adding song_ID
# Each song is unique, hence will have a unique song ID 
songs_limit = len(top_100_cleaned_df)+1
song_ID = range(1,songs_limit)
top_100_cleaned_df['song_ID'] = song_ID
# Grouping by artist spotify ID
artists = top_100_cleaned_df.groupby('artist_spotify_ID')['artist_name'].count()

print(f'There are a total of top {len(artists)} artists in the top 100 songs \nEach artist will be assigned a unique artist_ID')
# creating artist_df

artist_df = top_100_cleaned_df[['artist_name', 'artist_spotify_ID']]
artist_grouped_df = artist_df.drop_duplicates(['artist_spotify_ID'])

# displaying artist_df
artist_grouped_df
# generating csv file for album_table
artist_grouped_df.to_csv('Output_CSV/artist_df.csv', index = False)
# Grouping by album_name
albums = top_100_cleaned_df.groupby('album_name')['album_name'].count()

print(f'There are a total of top {len(albums)} albums in the top 100 songs \nEach album will be assigned a unique album_ID')
# creating album_df

album_df = top_100_cleaned_df[['album_name', 'album_type']]
album_grouped_df = album_df.drop_duplicates(['album_name'])

# displaying artist_df
album_grouped_df
# creating output csv for main table
album_grouped_df.to_csv('Output_CSV/album_df.csv', index=False)
# creating song_df
song_df = top_100_cleaned_df[['song_ID', 'song_title', 'album_name','track_spotify_ID', 'artist_spotify_ID', 'song_ranking', 'spotify_popularity', 'song_duration[ms]', 'song_release_date']]

# generating csv file for song_table
song_df.to_csv('Output_CSV/song_df.csv', index = False)

# displaying song_table
song_df
# Concert Data
import json
from api_keys import BIT_api
import pprint
import os
# converting artinst_names to list
artist_list = artist_grouped_df['artist_name'].tolist()

# printing the list
artist_list
# importing event_api function from events_api.py
import events_api
# generating event_df
event_df = event_api(artist_list)
# printing event_df
event_df
# generating csv file for concert_table
event_df.to_csv('Output_CSV/event_df.csv')

# displaying album_table
event_df
