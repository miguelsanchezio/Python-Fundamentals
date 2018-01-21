nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1] # 2
nested_list[-1][-2] # 8

for l in nested_list:
    for val in l:
        print(val)

coords = [[10.412, 8.1231], [31.1233, -13.41212], [21.34123, 31.124123]]

[['L' if num % 2 != 0 else 'O' for num in range(1, 4)] for val in range(1, 4)]
# [['L', 'O', 'L'], ['L', 'O', 'L'], ['L', 'O', 'L']]