from flask import Flask
from flask_cors import CORS
# from flask_socketio import SocketIO
#
#
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# socketio = SocketIO(app)
#
# if __name__ == '__main__':
#     socketio.run(app, debug=True)
#
#CORS
CORS(app)

from app import routes