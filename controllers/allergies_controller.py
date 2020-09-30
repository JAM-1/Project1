from flask import Flask, render_template, request, redirect
from models.allergy import Allergy
import repositories.allergy_repository as allergy_repository
from flask import Blueprint
allergy_blueprint = Blueprint("allergy", __name__)

# LIST ALLERGIES: ACTION
@allergy_blueprint.route("/allergies")
def animals():
    all_allergy = allergy_repository.select_all()
    return render_template("/allergies/index.html", all_allergy= all_allergy)

# DELETE ALLERGIES: ACTION
@allergy_blueprint.route("/allergies/<id>/delete", methods=['POST'])
def delete(id):
    allergy_repository.delete(id)
    return redirect("/allergies")

# PRESENT NEW ALLERGIES: FORM
@allergy_blueprint.route("/allergies/new")
def new_allergy():
    return render_template("/allergies/new.html")

# CREATE NEW ALLERGIES: ACTION
@allergy_blueprint.route("/allergies", methods=['POST'])
def create():
    name = request.form['name']
    new_Allergy = Allergy(name)
    allergy_repository.save(new_Allergy)
    return redirect("/allergies")

# EDIT ALLERGIES: FORM
@allergy_blueprint.route("/allergies/<id>/edit", methods=['POST'])
def edit(id):
    allergy = allergy_repository.select(id)
    return render_template('allergies/edit.html', allergy=allergy)

# UPDATE EDITED ANIMAL ACTION
@allergy_blueprint.route("/allergies/<id>", methods=['POST'])
def update(id):
    name = request.form['name']
    allergy = Allergy(name, id)
    allergy_repository.update(allergy)
    return redirect('/allergies')