from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.medical import Medical
from models.allergy import Allergy
from models.animal_allergy import AnimalAllergy

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.medical_repository as medical_repository
import repositories.allergy_repository as allergy_repository
import repositories.animalallergy_repository as animalallergy_repository

animals_blueprint = Blueprint("animals", __name__)

# LIST ANIMALS ACTION
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("/animals/index.html", all_animals= animals)

# DELETE ANIMAL ACTION
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete(id):
    animal_repository.delete(id)
    return redirect("/animals")

# PRESENT NEW ANIMAL FORM
@animals_blueprint.route("/animals/new")
def new_animal():
    all_owners = owner_repository.select_all()
    all_vets = vet_repository.select_all()
    return render_template("/animals/new.html", all_owners=all_owners, all_vets=all_vets)

# CREATE NEW ANIMAL ACTION
@animals_blueprint.route("/animals", methods=['POST'])
def create():
    name = request.form['name']
    type = request.form['type']
    dob = request.form['dob']
    owner_id = request.form['owner']
    vet_id = request.form['vet']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    new_Animal = Animal(name, type, dob, owner, vet)
    animal_repository.save(new_Animal)
    return redirect("/animals")

# EDIT ANIMAL FORM
@animals_blueprint.route("/animals/<id>/edit", methods=['POST'])
def edit(id):
    animal = animal_repository.select(id)
    all_owners = owner_repository.select_all()
    all_vets = vet_repository.select_all()
    return render_template('animals/edit.html', animal=animal, all_owners = all_owners, all_vets = all_vets)

# UPDATE EDITED ANIMAL ACTION
@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update(id):
    name = request.form['name']
    type = request.form['type']
    dob = request.form['dob']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    animal = Animal(name, type, dob, owner, vet, id)
    animal_repository.update(animal)
    return redirect('/animals')

# ANIMAL DATA: ACTION 
@animals_blueprint.route("/animals/<id>", methods=['GET'])
def view_animal(id):
    animal = animal_repository.select(id)
    history = medical_repository.select_all_med(id)
    allergy = animalallergy_repository.select_all_id(id)
    print(allergy)
    return render_template("animals/results.html", animal=animal, history=history, allergy=allergy)

# ADD MEDICAL HISTORY: FORM
@animals_blueprint.route("/animals/<id>/medical", methods=['POST'])
def add_medical(id):
    animal = animal_repository.select(id)
    return render_template("/animals/medical.html", animal=animal)


# ADD MEDICAL HISTORY: ACTION
@animals_blueprint.route("/animals", methods=['POST'])
def create_medical(id):
    description = request.form['description']
    new_history = Medical(description, id)
    medical_repository.save(new_history)
    return redirect("/animals")