import lxml.html
import requests

from lxml.cssselect import CSSSelector

class WordSearch():

    SEARCH_URL = 'https://duckduckgo.com/?q='

    def search(self, word):
        r = requests.get(self.SEARCH_URL + word)

        # Raise an exception if file could not be downloaded.
        r.raise_for_status()

        return self.getTitles(r.text)

    def getTitles(self, html):
        tree = lxml.html.fromstring(html)

        selector = CSSSelector('.result__title .result__a')

        results = selector(tree)[:3]

        titles = []
        for match in results:
            titles.append(match.text)

        return titles

