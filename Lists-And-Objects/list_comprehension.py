numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list) # ['1', '2', '3', '4', '5']

numbers_2 = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]