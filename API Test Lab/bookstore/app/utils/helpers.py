import json
import csv
import os
from datetime import datetime

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "..", "db-models", "books.csv")
cart_csv_path = os.path.join(current_dir, "..", "db-models", "book_cart.csv")


# *********************************************************************************************************
# convert dictionary to list :
def dict_to_list(dict_data, key_order, default_value=""):
    """
    Convert a dictionary to a list based on a specified key order.

    :param dict_data: The dictionary to convert.
    :param key_order: A list of keys in the order they should be extracted.
    :param default_value: The default value to use if a key is missing.
    :return: A list of values corresponding to the keys in key_order.
    """
    return [dict_data.get(key, default_value) for key in key_order]


# our header function is organized as follows:
key_order = [
    "authors",
    "categories",
    "num_pages",
    "published_year",
    "subtitle",
    "title",
]

# *********************************************************************************************************


# get books from csv
def get_books_from_csv(csvfile_path):
    books = []
    with open(csvfile_path, mode="r", encoding="ISO-8859-1", errors="replace") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


def filter_books(csv_path, attribute, value):
    filtered_books = []
    books = get_books_from_csv(csv_path)
    # print(f"Books: {books}")
    for book in books:
        if book[attribute] == str(value):
            filtered_books.append(book)
    # print(f"filtered books: {filtered_books}")

    return filtered_books


"""add book to cart """


def write_csv_data(loc, data=[]):
    with open(loc, "a", encoding="utf8", newline="") as file:
        # Init the csv writer
        csv_writer = csv.writer(file)

        # Write the data object's contents as rows
        # Each list inside of data[] becomes a new row
        # The first row will be interpreted as the csv's headers
        # print("data to be written:", data)
        csv_writer.writerows(data)

        # Close the file
        file.close()


def add_book_to_csv(bookInfo=[]):
    # Get the existing contents of the library
    data = get_books_from_csv(cart_csv_path)
    book_list = dict_to_list(bookInfo, key_order)
    # print(f"Book list: {book_list}")
    # Add the new book to the data
    data.append(book_list)

    # Write the new file
    try:
        print(f"book:-> {data}")
        write_csv_data(cart_csv_path, data)
        return True
    except Exception as e:
        print(Exception)
        return False


# test the function


# print(convert_csv_to_json(csv_path,"Year-Of-Publication","1995"))
# print("books:",get_books_from_csv(csv_path))
# print(filter_books(csv_path, "published_year", "2004"))
