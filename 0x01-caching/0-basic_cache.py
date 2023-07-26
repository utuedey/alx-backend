#!/usr/bin/env python3
"""
0-basic_cache module
A class that represent a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class that represents a basic cache.
    """
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None and key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
