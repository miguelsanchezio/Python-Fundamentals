f = open("story.txt")

# reads from start to finish, moves cursor to the end of file
f.read()

# moves the cursor
f.seek(0)

print(f.read())

f.seek(0)

# reads one line at a time
f.readline()

f.seek(0)

# returns a list of lines
f.readlines()

# closes the file
f.close()

# returns true of file is closed, false otherwise
f.closed

# opens the file and then closes the file after the block is resolved
with open("story.txt") as file:
    data = file.read()

