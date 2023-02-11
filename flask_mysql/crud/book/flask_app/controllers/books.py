from flask_app import app
from flask import Flask , render_template, request,session, redirect
from flask_app.models.user_model import User, Book
@app.route