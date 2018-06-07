# SyntaxError
def first: # SyntaxError
None = 1 # SyntaxError
return # SyntaxError

# NameError
test # NameError

# TypeError
len(5) # TypeError

# IndexError
list = 'hello'
list[43] # IndexError

# ValueError
int('foo') # ValueError

# KeyError
d = {}
d['foo'] # KeyError

# AttributeError
'awesome'.foo # AttributeError