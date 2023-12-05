from ..utils import helpers, validators
from flask import Blueprint, jsonify, current_app, request

main = Blueprint("main", __name__)

#List Books (/api/books)
@main.route("/api/books", methods=["GET"])
@validators.require_api_key
def get_books():
    # title,subtitle,authors,categories,published_year,num_pages
    attribute = request.args.get("attribute")
    value = request.args.get("value")

    try:
        #books = helpers.get_books_from_csv(helpers.csv_path)
        if attribute and value:
            filtered_books = helpers.filter_books(helpers.csv_path, attribute, value)
            return jsonify(filtered_books), 200
        else:
            books = helpers.get_books_from_csv(helpers.csv_path)
            #print(f"book :{books}")
            return jsonify(books), 200
    except Exception as e:
        current_app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500


#Display Single Book (/api/books/{isbn})
@main.route("/api/books/<isbn>", methods=["GET"])
@validators.require_api_key
def get_single_books(isbn):
    try:
        books = helpers.get_books_from_csv(helpers.csv_path)
        # Find the book with the given ISBN
        book = next((book for book in books if book['ISBN'] == isbn), None)
        if book:
            return jsonify(book), 200
        else:
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        current_app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500



@main.route("/api/<userID>/cart/add", methods=["POST"])
@validators.require_api_key
def add_new_book(userID):
    headers = request.headers
    print("userID:", userID)
    # Get the data from the POST request as json which is converted to a python list
    # The data sent is a list of info for a single book.
    data = request.get_json()
    print(type(data))
    # Call the update function to create the new library.
    helpers.create_cart_and_add_content(str(userID), "db-models", data)
    # helpers.add_book_to_csv(data)

    return data, f"{200}: data successfully added to cart "
