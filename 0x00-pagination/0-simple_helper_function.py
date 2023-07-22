#!/usr/bin/env python3
"""
0-simple_helper_function module.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Return a tuple of size two containing a start index
       and an end index corresponding to the range of indexes to
       return in a list for page and page_size"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
