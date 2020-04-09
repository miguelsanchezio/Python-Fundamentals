def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive."
    return x + y


add_positive_numbers(1, 1)
add_positive_numbers(1, -1)

# If a Python file is run with the -O flag,
# assertionsgi will not be evaluated