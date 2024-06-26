#!/usr/bin/env python3
""" implement get and put method in caching objects"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """add item too cached data"""
        if not key or not item:
            return None
        return self.cache_data.update({key: item})

    def get(self, key):
        """get item from cached data"""
        keys = self.cache_data.keys()
        if key is None or key not in keys:
            return None
        return self.cache_data.get(key)
