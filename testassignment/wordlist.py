import re
import requests

from pathlib import Path

class WordList():

    def file_exists(self):
        file = Path('words.txt')

        return file.is_file()

    def download_file(self):
        r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

        # Raise an exception if file could not be downloaded.
        r.raise_for_status()

        with open('words.txt', 'w') as file:
            for word in WordList.filter_valid_words(r.text):
                file.write(word)

    @staticmethod
    def filter_valid_words(words):
        return re.findall(r"\b[a-z][a-zA-Z]+\b", words, re.MULTILINE)
