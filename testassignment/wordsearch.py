import json
import lxml.html
import requests

from collections import OrderedDict
from lxml.cssselect import CSSSelector

class WordSearch():

    SEARCH_URL = 'https://duckduckgo.com/?q='

    def search(self, word):
        r = requests.get(self.SEARCH_URL + word)

        # Raise an exception if file could not be downloaded.
        r.raise_for_status()

        return self.get_titles(r.text)

    def get_titles(self, html):
        tree = lxml.html.fromstring(html)

        selector = CSSSelector('.result__title .result__a')

        results = selector(tree)[:3]

        titles = []
        for match in results:
            titles.append(match.text)

        return titles

    def get_json(self, words):
        results = OrderedDict()

        for word in words:
            titles = self.search(word)

            results[word] = titles

        return json.dumps(results)
