import json
import csv
import os
from datetime import datetime


current_dir = os.path.dirname(__file__)
# csv_path = os.path.join(current_dir, "..", "db-models", "books.csv")
csv_path = os.path.join(current_dir, "..", "db-models", "books_with_isbn.csv")
cart_csv_path = os.path.join(current_dir, "..", "db-models", "book_cart.csv")
unprocessed_file_path = os.path.join(current_dir, "..", "db-models", "random_users.csv")
processed_users_file_path = os.path.join(current_dir, "..", "db-models", "users.csv")
# processed_users_file_path = "./users.csv"

"""****Create file if it doesnt exist"""


def create_cart_and_add_content(filename, destination_folder, content):
    header_list = [key for key, value in content.items()]
    list_data = []
    list_data.append(content)
    with open(
        os.path.join(current_dir, "..", destination_folder, f"{filename}_cart.csv"),
        "a",
        newline="",
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header_list)
        writer.writeheader()
        writer.writerows(list_data)


#  *********************users.csv specific functionc*********************
# this function is specific to user data


def add_unique_id_to_csvdata(file_path, unique_id_header=str):
    new_data = []
    # convert csv to json
    with open(file_path, encoding="utf-8") as csvfile:
        csvReader = csv.DictReader(csvfile)
        firstInit = ""
        secondInit = ""
        num = 0
        # uniq_num = f"00{num}"
        userID = ""
        for row in csvReader:
            num = num + 1
            uniq_num = f"00{num}"
            for key, value in row.items():
                if key == "first_name":
                    firstInit = value[0]

                    # print(firstInit)
                if key == "last_name":
                    secondInit = value[0]
            userID = firstInit + secondInit + uniq_num
            helperdict = {unique_id_header: userID}
            new_row = {**helperdict, **row}
            new_data.append(new_row)
            # print(new_row)
    return new_data


# write the adjusted userdata to users.csv file
def write_data_to_existing_csv(list_of_dictionary_with_data, file_path):
    list_of_headers = []
    for each_item in list_of_dictionary_with_data:
        header_list = [key for key, value in each_item.items()]
        list_of_headers = header_list
    # print(list_of_headers)
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list_of_headers)
        writer.writeheader()
        writer.writerows(list_of_dictionary_with_data)


new_dictionary_users = add_unique_id_to_csvdata(unprocessed_file_path, "userID")
write_data_to_existing_csv(new_dictionary_users, processed_users_file_path)


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
    #print(books)
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


# *********************************add book to cart**********************


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
