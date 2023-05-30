import csv

# Open the input file for reading
with open('car_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row['make'] for row in reader]

# Open the output file for writing
with open('make_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['make'])  # Write the header
    writer.writerows([[value] for value in data])  # Write the make values row by row
