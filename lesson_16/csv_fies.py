import csv

with open('data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for row in data:
    last_name, name, city = row
    print(f'Last name: {last_name}, Name: {name}, City: {city}')
