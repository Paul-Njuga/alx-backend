#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits BaseCaching
    """

    def get(self, key):
        """Returns items in cache_data"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Inserts key, item into cache_data"""
        if key and item:
            self.cache_data[key] = item
