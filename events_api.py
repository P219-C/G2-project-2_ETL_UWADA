
import requests
import json
from api_keys import BIT_api
import pprint


def event_api(artists):
    
    url_base = "https://rest.bandsintown.com/artists"

    event_dict = {}

    for artist in artists:

        print(artist)
        url_query = f'{url_base}/{artist}/events?app_id={BIT_api}'
        
        request = requests.get(url_query)

        requested_event = (request.json())

        try:

            event_dict[artist] = [requested_event[0]['artist']['name'], requested_event[0]['venue']['name'], requested_event[0]['venue']['country'], requested_event[0]['venue']['location'], requested_event[0]['datetime'][0:10]]
            # pprint.pprint(event_dict[artist])

        except:

            event_dict[artist] = [404]

        

        # for event in requested_event:
        #     print("-------->>>>")
        #     pprint.pprint(event)
        


        # return requested_event[0]
    pprint.pprint(event_dict)

test = event_api(['adele', 'justin bieber', 'pablo crespo'])
