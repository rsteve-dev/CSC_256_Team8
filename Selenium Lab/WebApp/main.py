from flask import Flask, render_template, request, jsonify
import json
import csv

app = Flask(__name__)

@app.route("/")
def start_app():
    csv_data = get_csv_data('./static/books_short.csv')
    # Render the search.html file in templates folder and pass the csv data through
    return render_template('search.html', csv_data=csv_data)

@app.route("/process", methods=['POST'])
def process():
    data = request.get_json()

    return data

# Funtion to get the CSV file's data
def get_csv_data(loc):
    csv_data = []
    # Open the file and force UTF-8 encoding
    with open(loc, encoding="utf8") as file:
        # Read the file and put each row in a csv_data object
        csvReader = csv.DictReader(file)
        csv_data = [row for row in csvReader]
    return csv_data

