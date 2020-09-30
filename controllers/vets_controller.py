from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet
from models.animal import Animal
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vets_blueprint = Blueprint("vet", __name__)

# LIST VETS: ACTION 
@vets_blueprint.route("/employees")
def show_vets():
    all_vets = vet_repository.select_all()
    return render_template("/employees/index.html", all_vets=all_vets)

# DELETE VET: ACTION 
@vets_blueprint.route("/employees/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect ("/employees")

# NEW VET: PRESENT FORM
@vets_blueprint.route("/employees/new")
def new_vet():
    return render_template("/employees/new.html")

# CREATE NEW VET: ACTION 
@vets_blueprint.route("/employees", methods=['POST'])
def create_vet():
    name = request.form['name']
    contact = request.form['contact']
    new_Vet = Vet(name, contact)
    vet_repository.save(new_Vet)
    return redirect("/employees")

# EDIT VET: FORM 
@vets_blueprint.route("/employees/<id>/edit", methods=['POST'])
def edit_vet(id):
    vet = vet_repository.select(id)
    all_animal = animal_repository.select_all()
    return render_template("employees/edit.html", all_animal=all_animal, vet=vet)

# UPDATE EDITED VET: ACTION 
@vets_blueprint.route("/employees/<id>", methods=['POST'])
def update_vet(id):
    name = request.form['name']
    contact = request.form['contact']
    vet = Vet(name, contact, id)
    vet_repository.update(vet)
    return redirect("/employees")


# SHOW VET DATA: ACTION 
@vets_blueprint.route("/employees/<id>", methods=['GET'])
def view_vet(id):
    vet = vet_repository.select(id)
    all_animals = animal_repository.select_id(id)
    return render_template("employees/results.html", vet=vet, all_animals=all_animals)


