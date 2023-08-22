#!/usr/bin/env python3
'''
Basic dictionary caching
'''
BaseCaching = __import__('base_caching').BaseCaching


# class BasicCache(BaseCaching):
#     '''Basic caching class'''

#     def put(self, key, item):

#         if key == None or item == None:
#             return
#         self.cache_data[key] = item

#     def get(self, key):
#         if key == None:
#             return None
#         if key not in self.cache_data.keys():
#             return None
#         return self.cache_data[key]

class BasicCache(BaseCaching):
    ''' Basic Caching Class '''

    def put(self, key, item):
        ''' put method for putting a new key and item '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' get method for retrieving item stored in key '''
        return self.cache_data.get(key)
