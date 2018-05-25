# returns true of all items are truthy
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Christina']
all([name[0] == 'C' for name in people])

# returns true if any item is truthy
people2 = ['Charlie', 'Casey', 'Cody', 'Carly', 'Christina', 'Rick']
all([name[0] == 'R' for name in people2])