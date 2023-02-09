from flask_app import app
#!!! REmember to IMPORT ALLA ROUTES HERE FROM CONTROLLERS!!!!!!
from flask_app.controllers import users # les noms des tables de BD elli 3Anna fel conbtrolers

if __name__=='__main__':
    app.run(debug=True, port=5001)