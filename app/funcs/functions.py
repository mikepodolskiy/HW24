# reading file using generator
def read_file(filepath):
    with open(filepath, mode='r', encoding='UTF-8') as file:
        for line in file:
            yield line


# filtering data by value consistence
def filter_data(data, value):
    return filter(lambda x: value in x, data)


# output one col acc to col number
def map_data(data, value):
    col = int(value)
    return map((lambda line: line.split(' ')[col]), data)


# sorting data asc or desc form value argument
def sort_data(data, value):
    if value == 'asc':
        return sorted(data, reverse=False)
    if value == 'desc':
        return sorted(data, reverse=True)


# limiting data to show
def limit_data(data, value):
    limit = int(value)
    return list(data)[:limit]


# showing only unique data
# args, kwargs добавляются чтобы соблюсти единообразие аргументов используемых функций
def unique_data(data, *args, **kwargs):
    return set(data)
