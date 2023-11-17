from app import create_app

# Optionally, you can use configuration settings from an environment variable or a default one
app = create_app('development')

if __name__ == '__main__':
    # Run the Flask application
    # you can run the The host='0.0.0.0' this makes the server publicly available
    # You can specify the port as well, default is 5000 but might be in use 
    app.run(host='127.0.0.1', port=3000, debug=True)
