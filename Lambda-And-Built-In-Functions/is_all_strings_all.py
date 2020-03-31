def is_all_strings(iterable):
    return all(type(name) is str for name in iterable)