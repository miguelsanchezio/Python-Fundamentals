# for loops
for char in range(1,11):
  print(char)

for letter in 'coffee':
  print(letter * 10)

# ranges
nums = range(10, 100, 5)
print(list(nums))

# while loops
msg = input('What\'s the secret password? ')
while msg != '10X':
  print('Nope.')
  msg = input('So, what\'s the secret password? ')
print('Correct!')

# converting for loop to while loop

for num in range(1, 11):
    print(num)

num = 1
while num < 11:
  print(num)
  num += 1