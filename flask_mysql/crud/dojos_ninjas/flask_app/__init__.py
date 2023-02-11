from flask import Flask
app = Flask(__name__)
#! Session Key is required 
app.secret_key = "Trust the process"
DATABASE = "dojos_ninjas" #nom de la base de données