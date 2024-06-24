#!/usr/bin/env python3
""" simple pagination """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return page by index"""
        assert (
            isinstance(page, str) is False
            and isinstance(page_size, str) is False
        )
        assert page > 0 and page_size > 0
        data_set = self.dataset()
        start_index, end_index = self.index_range(page, page_size)
        if len(data_set) < start_index or len(data_set) < end_index:
            return []
        return data_set[start_index:end_index]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """index the page"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)
