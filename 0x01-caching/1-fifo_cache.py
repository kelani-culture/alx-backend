#!/usr/bin/env python3
""" Implement FIFO cache system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The FIFO cache objects system"""

    def put(self, key, item):
        """add itemt to the cache dict"""
        if key is None or item is None:
            return None

        self.cache_data.update({key: item})
        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")

        return self.cache_data

    def get(self, key):
        """get cached item"""
        return self.cache_data.get(key) or None