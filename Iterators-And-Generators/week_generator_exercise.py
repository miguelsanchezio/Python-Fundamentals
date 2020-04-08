def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counter = 0
    while counter < len(days):
        yield days[counter]
        counter += 1


w = week()

for d in w:
    print(d)
