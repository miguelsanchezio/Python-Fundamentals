def yes_or_no():
    counter = 2
    while True:
        if counter % 2 == 0:
            counter += 1
            yield "yes"
        else:
            counter += 1
            yield "no"


gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))