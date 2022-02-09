from typing import *


class URL:
    def __init__(
        self,
        base_url: Optional[str] = None,
        suffix: Optional[str] = None,
        filter: bool = False,
        search: bool = False,
        range: bool = False,
        sorting: bool = False,
        pagination: bool = False,
        API_KEY: Optional[str] = None,
    ):
        if API_KEY:
            self.set_api_key(API_KEY)

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        if filter:
            self.apply_filter()

        if search:
            self.apply_search()

        if range:
            self.apply_range()

        if sorting:
            self.apply_sorting()

        if pagination:
            self.apply_pagination()

    def set_base_url(self, base_url: str = "") -> int:
        self.base_url = base_url
        return 0

    def set_api_key(self, API_KEY: str) -> int:
        self.API_KEY = API_KEY
        return 0

    def apply_filter(self, filter_options: dict[str, int]) -> str:
        return self.base_url

    def apply_search(self, search_options: dict[str, int]) -> str:
        return self.base_url

    def apply_range(self, range_options: dict[str, int]) -> str:
        return self.base_url

    def apply_sorting(self, sorting_options: dict[str, int]) -> str:
        return self.base_url

    def apply_pagination(self, pagination_options: dict[str, int]) -> str:
        return self.base_url
