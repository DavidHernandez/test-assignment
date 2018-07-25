from http.server import BaseHTTPRequestHandler, HTTPServer

from cache import Cache, InvalidCacheKeyException
from wordsearch import WordSearch

class WordSearchService(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/search/duckduckgo/" not in self.path:
            self.send_response(404)
            return

        path_elements = self.path.split('/')
        if len(path_elements) != 4:
            self.send_response(404)
            return

        word = path_elements[3]
        if word == '':
            self.send_response(404)
            return

        json = self.get_word(word)

        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()

        self.wfile.write(bytes(json, "utf8"))
        return

    def get_word(self, word):
        cache = Cache()
        try:
            json = cache.get(word)
        except InvalidCacheKeyException:
            json = WordSearch().get_json([word])
            cache.set(word, json)

        return json

def main():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, WordSearchService)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
