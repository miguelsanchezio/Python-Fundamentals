max(3, 41, 55) # 55
max('c', 'd', 'a') # d

min(3, 41, 55) # 3
min('c', 'd', 'a') # a

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
min(len(name) for name in names)

max(names, key=lambda n: len(n)) # Ollivander