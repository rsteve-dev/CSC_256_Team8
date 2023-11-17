from app import create_app

# Optionally, you can use configuration settings from an environment variable or a default one
app = create_app('development')

if __name__ == '__main__':
    # Run the Flask application
    # The host='0.0.0.0' makes the server publicly available
    # You can specify the port as well, default is 5000
    app.run(host='127.0.0.1', port=3000, debug=True)