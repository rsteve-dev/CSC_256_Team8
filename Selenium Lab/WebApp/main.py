from flask import Flask, render_template, request, jsonify
import json
import csv

app = Flask(__name__)

LIBRARY_CSV_PATH = './static/csv/books_short.csv'

@app.route("/")
def start_app():
    csv_data = get_csv_data(LIBRARY_CSV_PATH)
    # Render the search.html file in templates folder and pass the csv data through
    return render_template('search.html', csv_data=csv_data)

@app.route("/receive_AJAX_POST", methods=['POST'])
def receive_AJAX_POST():
    data = request.get_json()
    print(data)
    return data

@app.route("/add_new_book", methods=['POST'])
def add_new_book():

    # Get the data from the POST request as json which is converted to a python list
    # The data sent is a list of info for a single book.
    data = request.get_json()

    # Call the update function to create the new library.
    add_book_to_csv(data)

    return data



# Funtion to get the CSV file's data
def get_csv_data(loc):
    csv_data = []
    # Open the file and force UTF-8 encoding
    with open(loc, 'r', encoding="utf8") as file:
        # Read the file and put each row in a csv_data object
        #csvReader = csv.DictReader(file)
        #csv_data = [row for row in csvReader]

        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)

    file.close()

    return csv_data



# Function to write csv file at parameter loc
# param loc = Location of file including file name
# param data = A list of lists containing data to write. The first entry is considered the csv's headers
def write_csv_data(loc, data = []):

    with open(loc, 'w', encoding="utf8", newline='') as file:

        # Init the csv writer 
        csv_writer = csv.writer(file)

        # Write the data object's contents as rows
        # Each list inside of data[] becomes a new row
        # The first row will be interpreted as the csv's headers
        csv_writer.writerows(data)

        # Close the file
        file.close()



# Function to add a new book
# param bookInfo = A list of a book's information
def add_book_to_csv(bookInfo = []):

    # Get the existing contents of the library
    data = get_csv_data(LIBRARY_CSV_PATH)

    # Add the new book to the data
    data.append(bookInfo)

    # Write the new file
    try:
        write_csv_data(LIBRARY_CSV_PATH, data)
        return True
    except Exception as e:
        print(Exception)
        return False