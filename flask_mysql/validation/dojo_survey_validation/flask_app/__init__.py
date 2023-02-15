from flask import Flask
app = Flask(__name__)
#! Session Key is required 
app.secret_key = "Trust the process"
DATABASE = "dojo_survey" #nom de la base de données