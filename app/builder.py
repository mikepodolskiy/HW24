from app.funcs.functions import filter_data, map_data, sort_data, limit_data, unique_data, regex_data_filter
from typing import Optional, Iterable, Callable

CMD_TO_FUNCTIONS: dict[str, Callable] = {'filter': filter_data,
                                         'map': map_data,
                                         'sort': sort_data,
                                         'limit': limit_data,
                                         'unique': unique_data,
                                         'regex': regex_data_filter}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable]) -> list[str]:
    if data is None:
        prepared_data: Iterable = read_file(file_name)

    else:
        prepared_data = data
    func: Callable = CMD_TO_FUNCTIONS[cmd]
    result: Iterable = func(data=prepared_data, value=value)
    return list(result)
