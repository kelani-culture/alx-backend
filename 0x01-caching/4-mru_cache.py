#!/usr/bin/env python3
""" Implement the MRU cache system algorithm"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching objects"""

    def __init__(self):
        """reinitialize the MRU BASE CACHING"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item too caching system"""
        if key is None or item is None:
            return

    def put(self, key, item):
            """Adds an item in the cache.
            """
            if key is None or item is None:
                return
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    mru_key, _ = self.cache_data.popitem(False)
                    print("DISCARD:", mru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ retrieve value from MRU cache"""
        val = self.cache_data.get(key) or None
        if not val:
            return None
        self.cache_data.move_to_end(key, False)
        return val