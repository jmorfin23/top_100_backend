from flask import Flask
from flask_cors import CORS




app = Flask(__name__)

#CORS
CORS(app)

from app import routes
