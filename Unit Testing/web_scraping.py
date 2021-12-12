from bs4 import BeautifulSoup
import requests


def web_scraping():
    """
    Scrapes the Billboard webpage (https://www.billboard.com/charts/hot-100/) to extract information of the hot 100 songs.

    returns:
    - a list of lists with rankings, artists and songs (100 entries)
    """
    # URL of pages to be scraped
    hot_url = "https://www.billboard.com/charts/hot-100/"
    # url2_artist100 = "https://www.billboard.com/charts/artist-100/"

    # Retrieving pages with the request method
    hot_response = requests.get(hot_url)
    # response_artist = requests.get(url2_artist100)

    # Creating BeautifulSoup objects; parse with 'html.parser'
    hot_soup = BeautifulSoup(hot_response.text, 'html.parser')
    # artist_soup = BeautifulSoup(response_artist.text, 'html.parser')

    # print(hot_soup.prettify())

    # Working with Hot 100

    hot_results = hot_soup.find_all('div', class_='o-chart-results-list-row-container')
    # print(hot_results)

    hot_list = []

    for result in hot_results:

        # print(result)
        try:
            hot_song = result.find('h3', class_='c-title').text
            hot_ranking_artist = result.find_all('span', class_='c-label')

            hot_ranking = hot_ranking_artist[0].text

            if len(hot_ranking_artist) == 10:
                hot_artist = hot_ranking_artist[3].text
            else:
                hot_artist = hot_ranking_artist[1].text
            # print(len(hot_ranking_artist), hot_ranking_artist)

            hot_song = hot_song[1:len(hot_song)-1]
            hot_artist = hot_artist[1:len(hot_artist)-1]
            hot_ranking = hot_ranking[1:len(hot_ranking)-1]

            

            hot_list.append([hot_ranking, hot_artist, hot_song])
            # print(f'{hot_ranking}.- "{hot_song}" by {hot_artist}')

        except AttributeError as e:
            print(e)


    # print(len(hot_list))

    for hot_entry in hot_list:
        print(hot_entry)

    return hot_list