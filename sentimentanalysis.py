import csv

def read_positive(file_path):
    positive = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            category, attribute = row
            if category in positive:
                positive[category].append(attribute)
            else:
                positive[category] = [attribute]
    return positive

def read_negative(file_path):
    negative = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            category, attribute = row
            if category in negative:
                negative[category].append(attribute)
            else:
                negative[category] = [attribute]
    return negative

