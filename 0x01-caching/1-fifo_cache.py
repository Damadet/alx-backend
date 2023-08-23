#!/usr/bin/env python3
'''First in first out cache'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' First In First Out Cache System '''

    def __init_(self):
        super().__init__()

    def put(self, key, item):
        ''' Adds an item to the cache
            Removes first item if cache size is
            greater than BaseCaching.MAX_ITEMS
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(list(self.cache_data.keys())) > BaseCaching.MAX_ITEMS:
            keys = [key for key in self.cache_data.keys()]
            del self.cache_data[keys[0]]
            print(f"DISCARD: {keys[0]}")

    def get(self, key):
        '''get an item with specified key from cache'''
        return self.cache_data.get(key)
