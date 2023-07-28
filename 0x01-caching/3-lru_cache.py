#!/usr/bin/python3
"""
3-lru_cache module.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A class that represent the LRU caching replacement polices
    """
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        num_of_items = self.cache_data.keys()
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(num_of_items) > BaseCaching.MAX_ITEMS:
            list_of_keys = list(num_of_items)
            len_of_list = len(list_of_keys)
            del self.cache_data[list_of_keys[-len_of_list]]
            print(f'DISCARD: {list_of_keys[-len_of_list]}')

    def get(self, key):
        """Get an item by a key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
