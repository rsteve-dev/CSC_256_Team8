import json
import csv
import os
from datetime import datetime


#get books from csv
def get_books_from_csv(csvfile_path):
    books = []
    with open(csvfile_path, mode='r', encoding='ISO-8859-1',errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


#convert csv to json 
def filter_books(csvfile_path, attribute , value):
    matching_rows = []
    with open(csvfile_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row[attribute] == value:
                # Assuming 'id' is present in the CSV
                matching_rows.append(row)
    metadata = {
        "total_matching_rows": len(matching_rows),
        "filter_column": attribute,
        "filter_value": value,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    result = {
        "metadata": metadata,
        "data": matching_rows
    }

    return json.dumps(result, indent=4)        
 
#convert JSON to CSV
def convert_json_to_csv(json_record):
    return csv_record




#test the function
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, '..', 'db-models', 'books.csv')
#print(convert_csv_to_json(csv_path,"Year-Of-Publication","1995"))
#print("books:",get_books_from_csv(csv_path))