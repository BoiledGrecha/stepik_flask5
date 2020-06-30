import csv
with open("delivery_categories.csv", "r") as f:
    reader = csv.DictReader(f, delimiter = ",")
    for i in reader:
        print(i, type(i))