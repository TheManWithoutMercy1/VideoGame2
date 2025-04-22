import csv

def convert_csv(csv_file):
    level = []
    with open(csv_file , mode='r') as file:
        csv_File = csv.reader(file)
        for lines in csv_File:
            print(lines)
            level.append(lines)

    print(level)

convert_csv('Levels_CSV/Level1.csv')