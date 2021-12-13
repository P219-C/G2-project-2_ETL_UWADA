def search(table):
    #running spotipy search function
    song_search = table['song_title']
    # print(song_search)
    results = sp.search(q='track:' + table['song_title'], type = 'track')
    tracks = results ['tracks']['items']
    
    if len(tracks) == 0:
        print(f'Song details not found for {song_search}')

    else:
        #extracting spotify ID for the track **Important to make further API calls**
        table['track_spotify_ID'] = tracks[0]['id']
        table['artist_spotify_ID'] = tracks[0]['album']['artists'][0]['id']

        #top_100_scrapped_df: song_duration,release_date

        try:
            table['song_duration[ms]'] = tracks[0]['duration_ms']
        except:
            table['song_duration[ms]'] = np.nan 

        try:
            table['song_release_date'] = tracks[0]['album']['release_date']
        except:
            table['song_release_date'] = np.nan 

        try:
            table['spotify_popularity'] = tracks[0]['popularity']  
        except:
            table['spotify_popularity'] = np.nan 

        # album_table: album_type 
        try:
            table['album_name'] = tracks[0]['album']['name']
        except:
            table['album_name'] = np.nan 

        # album_table: album_type 
        try:
            table['album_type'] = tracks[0]['album']['album_type']
        except:
            table['album_type'] = np.nan 

    return table