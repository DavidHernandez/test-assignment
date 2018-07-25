class Cache():
    CACHE_FILE = 'cache'

    def get(self, key):
        try:
            with open(self.CACHE_FILE, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    if key + '|' in line:
                        position = line.find('|') + 1
                        return line[position:]
        except:
            raise InvalidCacheKeyException()

        raise InvalidCacheKeyException()

    def set(self, key, value):
        try:
            self.get(key)

        except InvalidCacheKeyException:
            self.write(key, value)

    def write(self, key, value):
        with open(self.CACHE_FILE, 'a') as file:
            file.write(key + '|' + value + "\n")

class InvalidCacheKeyException(Exception):
    pass
