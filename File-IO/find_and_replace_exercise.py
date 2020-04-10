def find_and_replace(file_name, word, new_word):
    with open(file_name, "r+") as file:
        content = file.read()
        new_content = content.replace("Alice", "Colt")
        file.seek(0)
        file.write(new_content)
        file.truncate()

find_and_replace("chapter1.txt", "Alice", "Colt")