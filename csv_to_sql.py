#!/usr/bin/python3


"""
This Python script converts the dictionary.csv
file for the Lexi_Vault project to SQL file.
"""
import csv as c


"""
CSV file input and SQL file output
file paths
"""
csv_file = 'dictionary.csv'
sql_file = 'test.sql'


"""
Define the SQL database
table schema
"""
table_name = 'dictionary'
columns = ['word_id', 'words', 'part_of_speech', 'meanings']


"""
Open CSV and SQL files
"""
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile, \
        open(sql_file, 'w', encoding='utf-8') as sqlfile:

    csvreader = c.reader(csvfile)
    next(csvreader)


    """
    Initialize the SQL 
    INSERT statement
    """
    sql_insert = F"INSERT INTO {table_name} ({', '.join(columns)}) VALUES "
    

    """
    SQL statements for converting 
    to SQL file
    """
    for idx, row in enumerate(csvreader, start=1):
        word_id = idx
        words = row[0].replace("'", "''")
        part_of_speech = row[1].replace("'", "''")
        meanings = row[2].replace("'", "''")


        """
        Generate and Append values to the 
        SQL INSERT statement
        """
        sql_insert += F"({word_id}, '{words}', '{part_of_speech}', '{meanings}'),"


    """
    Remove the trailing comma and
    close the statement
    """
    sql_insert = sql_insert.rstrip(',') + ';'


    """
    Write INSERT statement to SQL file
    """ 
    sqlfile.write(sql_insert)

