def say_hello():
    instructor = 'Larry'
    return f'Hello {instructor}'

say_hello()
print(instructor) # NameError


total = 0
def increment():
    global total += 1
    return total

increment()

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()