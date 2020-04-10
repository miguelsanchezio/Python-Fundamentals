from csv import DictWriter

with open("cats_2.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Shoe",
        "Breed": "Tuxie",
        "Age": 1
    })
    csv_writer.writerow({
        "Name": "Agatha",
        "Breed": "Tuxie",
        "Age": 3
    })