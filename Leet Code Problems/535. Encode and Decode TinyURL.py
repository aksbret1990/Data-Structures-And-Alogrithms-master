# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:39:35 2018

@author: Akshay Jagadale
"""

#class Codec:
#    
#    def __init__(self):
#        self.urls = []
#
#    def encode(self, longUrl):
#        """Encodes a URL to a shortened URL.
#        
#        :type longUrl: str
#        :rtype: str
#        """
#        self.urls.append(longUrl)
#        return 'http://tinyurl.com/' + str(len(self.urls) - 1)
#        
#
#    def decode(self, shortUrl):
#        """Decodes a shortened URL to its original URL.
#        
#        :type shortUrl: str
#        :rtype: str
#        """
#        return self.urls[int(shortUrl.split('/')[-1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

class Codec:

    import string
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        import random
        code= ''
        while longUrl not in self.url2code:
            for i in range(0,6):
                code = code + random.choice(Codec.alphabet)
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]
        
myobj = Codec()
k = myobj.encode('https://leetcode.com/problems/design-tinyurlxaxa')
print(k)
print(myobj.decode('http://tinyurl.com/'+ k))