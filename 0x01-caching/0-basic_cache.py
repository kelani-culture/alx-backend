#!/usr/bin/env python3
""" implement get and put method in caching objects"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The Basic Cache system object"""

    def put(self, key, item):
        """add item too cached data"""
        if not key or not item:
            return None
        return self.cache_data.update({key: item})

    def get(self, key):
        """get cached item"""
        return self.cache_data.get(key) or None