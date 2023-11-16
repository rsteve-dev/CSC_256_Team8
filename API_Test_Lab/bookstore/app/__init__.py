from flask import Flask
from .routes import main_routes  # Assuming routes/main_routes.py defines a blueprint
from config import config 

def create_app(config_name='default'):
    app = Flask(__name__)

    # Configure the app
    # You can use object-based configuration or environment variables
    app.config.from_object(config[config_name])
    # Register blueprints
    app.register_blueprint(main_routes.main)

    return app