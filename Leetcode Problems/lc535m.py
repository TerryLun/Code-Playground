"""
535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL.
"""
import random


class Codec:
    def __init__(self):
        self.ls = {}
        self.sl = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.ls:
            return 'http://tinyurl.com/' + self.ls[longUrl]
        else:
            s = hex(random.randint(1, 100000))[2:].rjust(5, '0')
            while s in self.sl:
                s = hex(random.randint(1, 100000))[2:].rjust(5, '0')
            self.ls[longUrl] = s
            self.sl[s] = longUrl
            return 'http://tinyurl.com/' + s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('/')[-1]
        return self.sl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
