
import requests
import json
from api_keys import BIT_api
import pprint
import pandas as pd
from datetime import datetime
import os


def event_api(artists):
    
    url_base = "https://rest.bandsintown.com/artists"

    event_list = []

    # print(artists)

    for artist in set(artists):

        # print(artist)
        url_query = f'{url_base}/{artist.lower()}/events?app_id={BIT_api}'
        # print(url_query)
        
        request = requests.get(url_query)

        requested_event = (request.json())

        try:

            event_list.append([artist, requested_event[0]['artist']['name'], requested_event[0]['venue']['name'], requested_event[0]['venue']['country'], requested_event[0]['venue']['location'], requested_event[0]['datetime'][0:10]])
            # pprint.pprint(event_dict[artist])

        except:

            event_list.append([artist, 'Not Found', 'Not Found', 'Not Found', 'Not Found', 'Not Found'])

        

        # for event in requested_event:
        #     print("-------->>>>")
        #     pprint.pprint(event)
    # print(event_list)

    call_date = datetime.today().strftime('%Y-%m-%d')

    event_df = pd.DataFrame(event_list, columns = ['input_artist', 'api_artist', 'venue', 'country', 'location', 'datetime'])
    print(event_df)

    # final_df = event_df.dropna()
    final_df = event_df.copy()
    final_df = final_df.drop(['api_artist'], axis=1)
    print(final_df)
    final_df.to_csv(f"Data sources\event_table_{call_date}.csv")
    # final_df.to_csv(os.path.join("Data_sources", f"event_table_{call_date}.csv"))


    # return event_df

test = event_api(['ADELE', 'justin bieber', 'ADELE', 'pablo crespo'])