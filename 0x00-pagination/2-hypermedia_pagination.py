#!/usr/bin/env python3
"""
1-simple_pagination module
contains Server class to paginate a dataset
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Return the correct pagination"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset
           (i.e. the correct list of rows)"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        correct_indexes = index_range(page, page_size)
        data_lists = self.dataset()
        list_of_rows = data_lists[correct_indexes[0]:correct_indexes[1]]
        return list_of_rows

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with below values"""
        prev_page = page - 1

        if prev_page < 1:
            prev_page = None

        next_page = page + 1
        if next_page > len(self.dataset())//page_size:
            next_page = None

        media = {"page_size": len(self.get_page(page, page_size)),
                 "page": page,
                 "data": self.get_page(page, page_size),
                 "next_page": next_page,
                 "prev_page": prev_page,
                 "total_pages": len(self.dataset())//page_size}
        return media
