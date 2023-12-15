import csv

csv_file = 'sample.csv'

try:
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            # Each row is already a list of strings
            print(row)
except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")