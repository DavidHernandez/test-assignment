import json
import lxml.html
import requests

from collections import OrderedDict
from lxml.cssselect import CSSSelector

class WordSearch():

    SEARCH_URL = 'https://duckduckgo.com/html?q='

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
            titles.append(match.text_content())

        return titles

    def get_json(self, words):
        results = OrderedDict()

        for word in words:
            try:
                titles = self.search(word)

                results[word] = titles
            except:
                # There was an error on the request. Maybe flood protection on?
                pass

        return json.dumps(results)
