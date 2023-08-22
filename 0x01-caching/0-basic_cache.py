#!/usr/bin/env python3
'''
BAsic dictionary caching
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Basic caching class'''

    def put(self, key, item):

        if key == None or item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key == None:
            return None
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
