# lists
demo_list = ['a', 1, 24, True, 5.123]
# print(len(demo_list))

tasks = list(range(1, 4))
# print(tasks)

# accessing values in a list
colors = ['red', 'blue', 'green']
# print(colors[0])
# print(colors[2])
'orange' in colors # False
'red' in colors # True

# iterating over lists
colors_2 = ['orange', 'violet', 'teal']
# for color in colors:
#     print(color)

numbers = [4, 21, 412, 41, 15]
# for num in numbers:
#     print(num * num)

colors_3 = ['magenta', 'crimson', 'emerald', 'ruby']
i = 0
# while i < len(colors_3):
#     print(f'{i}: {colors_3[i]}')
#     i += 1

# list methods
# append
data = [1, 2, 3]
data.append(4)
data.extend([5, 6, 7, 8])
data.insert(0, 0)