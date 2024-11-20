import sys
import os

# Add the backend folder to Python's path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models import User, Role
