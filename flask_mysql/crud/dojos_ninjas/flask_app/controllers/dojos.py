from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
#==================Route home==========================#
@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template ("index.html", all_dojos = all_dojos)

#==================Route GET form==========================#
@app.route('/dojos/new')
def add_dojo():
    return render_template ("new_dojo.html")
#==================Route POST form==========================#

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.create_dojo(request.form)
    return redirect("/")
    
#==================Route show one ==========================#
@app.route('/dojos/<int:dojo_id>/show')
def show_dojo(dojo_id):
    data_dict = {'id':dojo_id}
    this_dojo = Dojo.get_one(data_dict)
    return render_template ("show_dojo.html", this_dojo = this_dojo)
#==================Route GET edit==========================#
@app.route('/dojos/<int:dojo_id>/edit')
def edit_dojo(dojo_id):
    this_dojo = Dojo.get_one({'id':dojo_id})
    return render_template ("edit_dojo.html", this_dojo = this_dojo)

#==================Route POST edit==========================#
@app.route('/dojos/update', methods=['POST']) # fel post je n'ai pas besoin de l'id#
def update_dojo():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    dojo_id = request.form['id']
    Dojo.update_dojo(request.form)
    return redirect(f'/dojos/{dojo_id}/show')
#==================Route delete one ==========================#
@app.route("/dojos/<int:dojo_id>/delete")
def delete_dojo(dojo_id):
    data_dict = {'id': dojo_id}
    Dojo.delete_dojo(data_dict)
    return redirect("/")