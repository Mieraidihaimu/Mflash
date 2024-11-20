from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

from flask_cors import CORS

# Import routes
from backend.routes import register_routes

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'some-random-salt'

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from backend.models import User, Role

# Set up Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Register routes
register_routes(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
