'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

'''
class Codec:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}
        self.letter_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        
        shortUrl = ""
        for i in range(6):
            shortUrl += self.letter_string[int(random.uniform(1, 62)) % 62]
        index = 0
        while(shortUrl in self.short_to_long):
            if index < 5:
                shortUrl = shortUrl[:index] + self.letter_string[int(random.uniform(1, 62)) % 62] + shortUrl[index+1:]
            else:
                shortUrl = shortUrl[:index] + self.letter_string[int(random.uniform(1, 62)) % 62]
            index = (index+1) % 6
        self.short_to_long[shortUrl] = longUrl
        shortUrl = "http://tinyurl.com/" + shortUrl
        self.long_to_short[longUrl] = shortUrl 
        return shortUrl
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if len(shortUrl) < 6:
            return shortUrl
        shortUrl = shortUrl[-6:]
        if shortUrl in self.short_to_long:
            return self.short_to_long[shortUrl]
        else:
            return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
