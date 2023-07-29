#!/usr/bin/python3
"""
3-lru_cache module.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A class that represent the LRU caching replacement polices
    """
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        num_of_items = self.cache_data.keys()
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(num_of_items)+1 > BaseCaching.MAX_ITEMS:
                lru_item, _ = self.cache_data.popitem(True)
                print(f'DISCARD: {lru_item}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Get an item by a key"""
        if key is None or key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
