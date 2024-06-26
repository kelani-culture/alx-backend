#!/usr/bin/env python3
""" Implement LRU cache algorithm"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache object"""

    def __init__(self):
        """reinitialize the method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Implement the put method for adding"""
        if not key or not item:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {key}")

        return self.cache_data

    def get(self, key):
        """get cached value in object"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key)
