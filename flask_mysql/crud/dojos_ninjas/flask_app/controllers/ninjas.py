from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas/new')
def add_ninja():
    dojos  = dojo.Dojo.get_all()
    return render_template ("new_ninja.html", dojos = dojos)

@app.route('/ninjas')
def all_ninjas():
    all_ninjas= Ninja.get_all()
    return render_template ("all_ninjas.html", all_ninjas=all_ninjas)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.create_ninja(request.form)
    return redirect('/ninjas')

#==================Route show one ==========================#

@app.route('/ninjas/<int:ninja_id>/show')
def show_ninja(ninja_id):
    data_dict={'id':ninja_id}
    this_ninja = Ninja.get_one(data_dict)
    return render_template ("show_ninja.html", this_ninja= this_ninja)
#==================Route GET edit==========================#

@app.route('/ninjas/<int:ninja_id>/edit')
def edit_ninja(ninja_id):
    this_ninja = Ninja.get_one({'id':ninja_id})
    return render_template ("edit_ninja.html", this_ninja=this_ninja)

#==================Route POST edit==========================#
@app.route('/ninjas/update', methods=['POST']) # fel post je n'ai pas besoin de l'id#
def update_ninja():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    ninja_id = request.form['id']
    Ninja.update_ninja(request.form)
    return redirect(f'/ninjas/{ninja_id}/show')
#==================Route delete ==========================#

@app.route("/ninjas/<int:ninja_id>/delete")
def delete_ninja(ninja_id):
    data_dict = {'id': ninja_id}
    Ninja.delete_ninja(data_dict)
    return redirect('/ninjas')