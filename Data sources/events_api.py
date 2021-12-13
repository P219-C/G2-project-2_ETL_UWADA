def event_api(artists):
    
    url_base = "https://rest.bandsintown.com/artists"

    event_list = []

    for artist in set(artists):
        url_query = f'{url_base}/{artist.lower()}/events?app_id={BIT_api}'
        
        request = requests.get(url_query)

        requested_event = (request.json())

        try:
            event_list.append([artist, requested_event[0]['artist']['name'], requested_event[0]['venue']['name'], requested_event[0]['venue']['country'], requested_event[0]['venue']['location'], requested_event[0]['datetime'][0:10]])
        except:
            event_list.append([artist, 'Not Found', 'Not Found', 'Not Found', 'Not Found', 'Not Found'])

    event_df = pd.DataFrame(event_list, columns = ['artist_name', 'api_artist', 'venue', 'country', 'location', 'datetime'])
 
    final_df = event_df.copy()
    final_df = final_df.drop(['api_artist'], axis=1)
    
    return event_df