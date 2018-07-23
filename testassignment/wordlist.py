import random
import re
import requests

from pathlib import Path

class WordList():

    WORDS_FILE = 'words.txt'

    def file_exists(self):
        file = Path(self.WORDS_FILE)

        return file.is_file()

    def download_file(self):
        r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

        # Raise an exception if file could not be downloaded.
        r.raise_for_status()

        with open(self.WORDS_FILE, 'w') as file:
            for word in WordList.filter_valid_words(r.text):
                file.write(word + '\n')

    def get_random_words(self):
        if not self.file_exists():
            self.download_file()

        with open(self.WORDS_FILE, 'r') as file:
            words = file.readlines()

        lines = random.sample(range(len(words)), 100)

        selected_words = []
        for line in lines:
            selected_words.append(words[line])

        return selected_words

    @staticmethod
    def filter_valid_words(words):
        return re.findall(r"\b[a-z][a-zA-Z]+\b", words, re.MULTILINE)
