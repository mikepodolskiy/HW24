# import required libraries and modules
import re
from typing import Iterable, Iterator


# filtering data by value consistence
def filter_data(data: Iterable[str], value: str) -> Iterator[str]:
    return filter(lambda x: value in x, data)


# output one col acc to col number
def map_data(data: Iterable[str], value: str) -> Iterator[str]:
    col = int(value)
    return map((lambda line: line.split(' ')[col]), data)


# sorting data asc or desc form value argument
def sort_data(data: Iterable[str], value: str) -> list[str]:
    if value == 'desc':
        reverse = True
    else:
        reverse = False
    return sorted(data, reverse=reverse)


# limiting data to show
def limit_data(data: Iterable[str], value: str) -> list[str]:
    limit = int(value)
    return list(data)[:limit]


# showing only unique data
# args, kwargs added to keep arguments the same in all funcs (for validation)
def unique_data(data: Iterable[str], *args: str, **kwargs: str) -> set[str]:
    return set(data)


def regex_data_filter(data: Iterable[str], value: str) -> Iterator[str]:
    return filter(lambda x: re.search(value, x), data)
