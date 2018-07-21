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
            file.write(r.text)
