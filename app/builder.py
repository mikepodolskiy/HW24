from app.funcs.functions import filter_data, map_data, sort_data, limit_data, unique_data, regex_data_filter

CMD_TO_FUNCTIONS = {'filter': filter_data,
                    'map': map_data,
                    'sort': sort_data,
                    'limit': limit_data,
                    'unique': unique_data,
                    'regex': regex_data_filter}


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data
    func = CMD_TO_FUNCTIONS[cmd]
    result = func(data=prepared_data, value=value)
    return list(result)
