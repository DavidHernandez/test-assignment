import unittest

from testassignment.wordlist import WordList

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.wordList = WordList()

    def test_file_download(self):
        self.assertFalse(self.wordList.file_exists())
        self.wordList.download_file()
        self.assertTrue(self.wordList.file_exists())

if __name__ == '__main__':
    unittest.main()
