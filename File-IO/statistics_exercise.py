def statistics(file_name):
    with open(file_name) as file:
        lines = len(file.readlines())
        file.seek(0)
        words = len(file.read().split())
        file.seek(0)
        characters = len("".join(file.read()))
    return {'lines': lines, 'words': words, 'characters': characters}


stats = statistics("chapter1.txt")
print(stats)


# "words": sum(len(line.split(" ")) for line in lines)

