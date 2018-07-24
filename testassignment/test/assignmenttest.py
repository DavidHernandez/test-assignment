import os
import unittest
from unittest import mock
from unittest.mock import MagicMock

from testassignment.wordlist import WordList, filter_valid_words
from testassignment.wordsearch import WordSearch

class WordListTest(unittest.TestCase):

    def setUp(self):
        self.wordList = WordList()

    @classmethod
    def setUpClass(cls):
        try:
            os.remove(WordList.WORDS_FILE)
        except:
            pass

    def test_file_does_not_exist(self):
        self.assertFalse(self.wordList.file_exists())

    def test_file_download(self):
        self.wordList.download_file()
        self.assertTrue(self.wordList.file_exists())

    def test_words_filter(self):
        words = 'test Words that Meet the cr1ter1a 420'
        filtered_words = ['test', 'that', 'the']

        self.assertEqual(filter_valid_words(words), filtered_words)

    def test_get_random_words(self):
        self.assertNotEqual(self.wordList.get_random_words(), self.wordList.get_random_words())

# Mock for function get from requests
def get_request_mock(*args, **keywargs):
    class MockResponse:
        def __init__(self, html):
            self.text = html

        def raise_for_status(self):
            pass

    if args[0] == WordSearch.SEARCH_URL + 'test':
        return MockResponse(sampleHtml)

class WordSearchTest(unittest.TestCase):

    def setUp(self):
        self.wordSearch = WordSearch()

    @mock.patch('requests.get', side_effect=get_request_mock)
    def test_word_search(self, mock):
        titles = self.wordSearch.search('test')

        self.assertEqual(titles, ['first title', 'second title', 'third title'])

    def test_json_output(self):
        self.wordSearch.search = MagicMock(return_value=['title 1', 'title 2', 'title 3'])

        titles = self.wordSearch.get_json(['test', 'cow'])

        self.assertEqual(titles, '{"test": ["title 1", "title 2", "title 3"], "cow": ["title 1", "title 2", "title 3"]}')


if __name__ == '__main__':
    unittest.main()

sampleHtml = '<html><head></head><body><div class="result__title"><a class="result__a">first title</a></div><div class="result__title"><a class="result__a">second title</a></div><div class="result__title"><a class="result__a">third title</a></div></body></html>'
