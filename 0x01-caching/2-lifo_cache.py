#!/usr/bin/env python3
""" Implement LIFO Cache system """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """The LIFO cache objects system"""

    def put(self, key, item):
        """Add item to the caching object"""
        if not key or not item:
            return None

        self.cache_data.update({key: item})
        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            last_item = list(self.cache_data.keys())[-1]
            del self.cache_data[last_item]
            print(f"DISCARD: {last_item}")

        return self.cache_data

    def get(self, key):
        """get cached item in object"""
        return (
            self.cache_data.get(key)
            if self.cache_data.get(key) or key in self.cache_data
            else None
        )
