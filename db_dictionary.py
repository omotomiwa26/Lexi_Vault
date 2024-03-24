import csv
import re

input_file = 'dictionary.csv'
output_file = 'db_dictionary.csv'

with open(input_file, 'r', newline='', encoding='utf-8', errors='ignore') as csvfile:
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(outfile)
        
        for row in csvreader:
            if len(row) > 0:  # Check if the row is not empty
                match = re.match(r'^(.*?) \((.*?)\) (.*)$', row[0])
                if match:
                    words = match.group(1).strip()
                    part_of_speech = match.group(2).strip()
                    meanings = match.group(3).strip()
                    csvwriter.writerow([words, part_of_speech, meanings])
                else:
                    print(f"Error processing row: {row[0]}")
            else:
                print("Empty row encountered")
