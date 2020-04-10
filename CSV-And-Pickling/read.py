from csv import reader, DictReader


# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")


# reader() doesn't give a list by default, it gives an iterator, a generator


# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row["Name"])