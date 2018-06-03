def sum_floats(*args):
    return sum(num for num in args if type(num) == float)