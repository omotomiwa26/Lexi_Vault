import csv

output_file = 'db_dictionary.csv'
sql_output_file = 'lexi_vault_db.sql'

# Open the output CSV file for reading
with open(output_file, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Open the SQL output file for writing
    with open(sql_output_file, 'w', encoding='utf-8') as sqlfile:
        # Write the SQL statements header
        sqlfile.write('INSERT INTO dico (words, part_of_speech, meanings) VALUES ')
        
        # Initialize an empty list to store the formatted rows
        rows = []
        
        # Iterate over each row in the CSV file
        for row in csvreader:
            # Format the row data for SQL
            words = row[0].replace("'", "''")  # Escape single quotes
            part_of_speech = row[1].replace("'", "''")  # Escape single quotes
            meanings = row[2].replace("'", "''")  # Escape single quotes
            
            # Add the formatted row to the list
            rows.append(f"('{words}', '{part_of_speech}', '{meanings}')")
        
        # Join all the formatted rows with commas and write to the SQL file
        sqlfile.write(',\n'.join(rows))
        # Write a semicolon to terminate the INSERT statement
        sqlfile.write(';')
