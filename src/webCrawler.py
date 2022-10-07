from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests

def  webcrawler():
    URL = "https://cbu.edu/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    print(soup)


if __name__ == "webcrawler":
    webcrawler()