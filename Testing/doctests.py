def add(a, b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    >>> add(51,49)
    100
    >>> add(29, 2)
    31
    """
    return a + b


def double(values):
    """
    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    >>> double([])
    []
    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    >>> double([2, 5])
    [4, 10]
    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * val for val in values]


def say_word(word):
    """
    >>> say_word("LOL")
    'LOL'
    >>> say_word("LMAO")
    'LMAO'
    >>> say_word(":P")
    ':P'
    """
    return word


def true_that():
    """
    >>> true_that()
    True
    """
    return True


def make_dict(keys):
    """
    >>> make_dict(['a', 'b'])
    {'b': True, 'a': True}
    >>> make_dict([1, 2, 3])
    {1: True, 2: True, 3: True}
    """
    return {key: True for key in keys}

# python3 -m doctest -v file_name.py
# white space and quotations matter
