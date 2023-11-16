from ..utils import helpers
from flask import Blueprint ,jsonify,current_app,request

main = Blueprint('main', __name__)


@main.route('/api/books', methods=['GET'])
def get_books():
    #title,subtitle,authors,categories,published_year,num_pages
    attribute =  request.args.get('attribute')
    value =request.args.get('value')
    
    try:
        books = helpers.get_books_from_csv(helpers.csv_path)
        if attribute and value:
            books=helpers.filter_books(helpers.csv_path,attribute,value.strip("'"))
            #return books,200
            return jsonify(books), 200
            
        else:
            books = helpers.get_books_from_csv(helpers.csv_path)
            return jsonify(books), 200
    except Exception as e:
        current_app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500
        
