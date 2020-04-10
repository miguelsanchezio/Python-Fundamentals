from csv import reader, writer

with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[i.upper() for i in row] for row in csv_reader]

with open("loud_fighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)
