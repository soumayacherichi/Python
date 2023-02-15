from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request, session, flash
# ==========================Index Page ===========================

@app.route('/')
def index():
    return render_template('index.html')

# ==========================Process ===========================

@app.route("/process", methods=["post"])
def process():
    if Dojo.validate(request.form):
        data = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment'],
        }
        dojo_id= Dojo.create_dojo(data)
        session['dojo_id']=dojo_id
        return redirect('/result')
    return redirect('/')
# ==========================Result Page ===========================

@app.route("/result")
def result():
    logged_dojo = Dojo.get_by_id ({'id': session['dojo_id']})
    return render_template("result.html", logged_dojo=logged_dojo) # bech n5arjouha fel display html


# ==========================Clear ===========================

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")
