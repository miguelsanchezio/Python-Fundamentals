from random import choice

# we can pass functions as arguments to other functions
def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(3, cube))
print(sum(3, square))

# we can return functions from other functions
def make_laugh_func(name):
    def get_laugh():
        laugh = choice(("HAHA", "LOL", "LMAO"))
        return f"{laugh} {name}"
    return get_laugh

laugh_at = make_laugh_func("Joe")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())