# immutable
months = ('January', 'February', 'March', 'April', 'May', 'June')
february = months[1]

for month in months:
    print(month)

i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1

# tuples methods
months.count('January') # 1
months.index('March') # 2

# tuples can be nested
nums = (1, 2, 3, (4, 5), 6, 7)

# tuples can be sliced
nums[1:4] # (2, 3, (4, 5))

# can be used as keys in dictionaries
locations = {
    (32.1412, 34.4123): 'Tokyo Office',
    (12.5412, -12.4121): 'New York Office',
    (31.4541, 12.4211): 'San Francisco Office'
}

# dictionary.items() returns tuples