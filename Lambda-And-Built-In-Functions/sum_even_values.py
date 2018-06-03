def sum_even_values(*args):
    even_values = list(filter(lambda n: n % 2 == 0, args))
    return sum(even_values)