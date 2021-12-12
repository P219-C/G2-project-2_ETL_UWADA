from bs4 import BeautifulSoup
import requests
import web_scraping


def test_web_scraping():
    test_list = web_scraping.web_scraping()
    
    # Test
    assert len(test_list) > 0