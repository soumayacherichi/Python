from flask_app import app
from flask import Flask , render_template, request,session, redirect
from flask_app.models.user_model import User

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/process", methods=["post"])
def process_form():
    print (f"FORM from request=={request.form}")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    User.create_user(request.form) #houni ba3d ma3malna la creation de methode fi user model neditelha houni pour qu'elle s'applique
    return redirect("/display")

@app.route("/display")
def display():
    users = User.get_all() # pour avoir toute la liste 
    return render_template("display.html", users=users) # bech n5arjouha fel display html

@app.route("/show_user/<int:user_id>")
def show_user(user_id):
    data_dict = {'id': user_id}
    user = User.get_one(data_dict)
    return render_template("one_user.html", user=user) 

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/display")