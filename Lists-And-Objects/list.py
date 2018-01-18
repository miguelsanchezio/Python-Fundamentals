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
# append, extend, insert, clear, pop, remove, clear
data = [1, 2, 3]
data.append(4)
data.extend([5, 6, 7, 8])
data.insert(0, 0)

data_2 = [1, 2, 3, 4, 4, 4, 5, 6]
data_2.pop() # popped 6
data_2.pop(1) # popped 2
data_2.remove(4) # [1, 2, 3, 4, 4, 5, 6]
data_2.clear() # clears the list

data_3 = [5, 6, 7, 8, 9, 10]
data_3.index(6) # 2
data_3.index(6, 1) # 1
data_3.index(8, 2, 5) #3

data_4 = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
data_4.count(2) # 3
data_4.count(21) # 0
data_4.count(3) # 2

data.reverse() # [3, 2, 1]

data_5 = ['Roguer', 'Zelda', 'Alex']
data_5.sort() # ['Alex', 'Roger', 'Zelda']

data_6 = ['Coding', 'is', 'fun!']
' '.join(data_6) # 'Coding is fun!'