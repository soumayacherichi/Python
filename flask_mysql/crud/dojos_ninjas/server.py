from flask_app import app
#! Always remember to import all routes here ( all controllers)
from flask_app.controllers import dojos, ninjas
if __name__ == '__main__':
    app.run(debug=True, port=5001)