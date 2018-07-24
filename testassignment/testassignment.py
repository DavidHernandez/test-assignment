from wordlist import WordList
from wordsearch import WordSearch

def main():
    wordList = WordList().get_random_words()
    wordSearch = WordSearch().get_json(wordList)

    print(wordSearch)

if __name__ == '__main__':
    main()
