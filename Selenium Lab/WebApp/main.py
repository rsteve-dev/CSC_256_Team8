from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

@app.route("/")
def start_app():
    csv_data = get_csv_data()
    return render_template('search.html', csv_data=csv_data)

def get_csv_data():
    csv_data = []
    with open('./static/books_short.csv', encoding="utf8") as file:
        csvReader = csv.DictReader(file)
        csv_data = [row for row in csvReader]
    return csv_data