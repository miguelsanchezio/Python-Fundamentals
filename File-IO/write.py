# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!\n")
    file.write("\n")

# a - append to the end of the file, preserving original contents
# NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out\n")
    file.write("\n")

# r+, by default cursor starts at 0, it can overwrite lines
# it only works with an existing file
with open("haiku.txt", "r+") as file:
    file.seek(10)
    file.write("ADDED USING r+")