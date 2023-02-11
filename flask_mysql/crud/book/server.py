from flask_app import app
#!!! REmember to IMPORT ALL ROUTES HERE FROM CONTROLLERS!!!!!!
from flask_app.controllers import users, books # les noms des tables de BD elli 3Anna fel controllers


if __name__=='__main__':
    app.run(debug=True, port=5001)