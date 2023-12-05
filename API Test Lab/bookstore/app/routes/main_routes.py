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
    data = request.get_json()

    # Assuming `create_cart_and_add_content` returns None if the book doesn't exist
    result = helpers.create_cart_and_add_content(str(userID), "db-models", data)

    if result is None:
        # If the book doesn't exist, return a 404 error
        return jsonify({"error": "Book not found"}), 404

    # Verify if all required fields are present in the data
    required_fields = ['ISBN', 'authors', 'categories', 'num_pages', 'published_year', 'subtitle', 'title']
    if not all(field in data for field in required_fields):
        # If any required field is missing, return a 400 Bad Request
        return jsonify({"error": "Missing required book fields"}), 400

    # If everything is okay, return the book data with a 201 status
    return jsonify(data), 201