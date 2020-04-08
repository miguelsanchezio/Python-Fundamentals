def get_multiples(num=1, count=10):
    i = num
    for n in range(count):
        yield i
        i += num


e = get_multiples(1, 10)

print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))