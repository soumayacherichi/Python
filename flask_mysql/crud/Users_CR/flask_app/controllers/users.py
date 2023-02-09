from flask_app import app
from flask import Flask , render_template, request,session, redirect
from flask_app.models.user_model import User

@app.route("/")
def form():
    return render_template("readall.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/process", methods=["post"])
def process_form():
    print (f"FORM from request=={request.form}")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    User.create_user(request.form) #houni ba3d ma3malna la creation de methode fi user model neditelha houni pour qu'elle s'applique
    return redirect("/display")

@app.route("/display")
def display():
    users = User.get_all() # pour avoir toute la liste 
    return render_template("readall.html", users=users) # bech n5arjouha fel display html


@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/display")
