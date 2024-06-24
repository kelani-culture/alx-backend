#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index the page"""
    return (page, page_size)
