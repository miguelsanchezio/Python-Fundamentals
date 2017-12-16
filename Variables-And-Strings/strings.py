# strings can be declared using single or double quotes
python_str = 'Single Quotes'
pythong_other_str = "Double Quotes"
python_quotes_in_quotes = "Quotes can be 'used' together."

# string escape characters / escape sequences
new_line = 'Hello \n world'
print(new_line)

backslash = 'Hello \\ backslash'
print(backslash)

quotes = 'Hello \'world\''
print(quotes)

# string concatenation
str_one = 'The'
str_two = '10X Rule'
ten_ex = str_one + ' ' + str_two
print(ten_ex)

name = 'Miguel'
name += ' Sanchez'
print(name)

# string formatting
# f strings
guess = 8
print(f'Your guess of {guess} was correct.')
#old way
print('Your {} was correct.'.format(guess))