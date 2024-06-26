#!/usr/bin/env python3
""" Implement LIFO Cache system """
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """The LIFO cache objects system"""

    def __init__(self):
        """reinitialize the cached data object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to the caching object"""
        if not key or not item:
            return None

        if BaseCaching.MAX_ITEMS < len(self.cache_data) + 1:
            last_item = self.cache_data.popitem(True)
            print(f"DISCARD: {last_item[0]}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data

    def get(self, key):
        """get cached item in object"""
        return self.cache_data.get(key) or None
