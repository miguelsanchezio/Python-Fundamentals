# sets hold unique values
new_set = {1, 2, 3, 4, 'string', 12.31}

for thing in new_set:
    print(thing)

2 in new_set # True
22 in new_set # False

# methods
new_set2 = {1, 2}

new_set2.add(3)
new_set2.remove(1)
new_set2.discard(2) # throws no errors
new_set3 = new_set2.copy()
new_set3.clear()

# math
# generates a set with all unique students
math_students = {'Tony', 'Rick', 'Andy'}
# generates a set with students who are in both courses
biology_students = {'Grant', 'Andy', 'Oliver'}

math_students | biology_students # {'Tony', 'Rick', 'Andy', 'Grant', 'Oliver'}
math_students & biology_students # {'Andy'}