import os
import unittest

from testassignment.wordlist import WordList, filter_valid_words

class SearchTest(unittest.TestCase):

    def setUp(self):
        try:
            os.remove(WordList.WORDS_FILE)
        except:
            pass

        self.wordList = WordList()

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

if __name__ == '__main__':
    unittest.main()
