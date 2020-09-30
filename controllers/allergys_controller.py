from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal_allergy import AnimalAllergy
import repositories.animalallergy_repository as animalallergy_repository
import repositories.animal_repository as animal_repository
import repositories.allergy_repository as allergy_repository

allergys_blueprint = Blueprint("allergys", __name__)

# LIST
@allergys_blueprint.route("/allergys")
def animals():
    all_animals = animal_repository.select_all()
    all_allergies = allergy_repository.select_all()
    return render_template("/allergys/index.html", all_animals= all_animals, all_allergies=all_allergies)

# CREATE NEW ANIMAL ACTION
@allergys_blueprint.route("/allergys", methods=['POST'])
def create():
    allergy_id = request.form['allergy']
    animal_id = request.form['animal']
    allergy = allergy_repository.select(allergy_id)
    animal = animal_repository.select(animal_id)
    new_animal_allergy = AnimalAllergy(animal, allergy)
    animalallergy_repository.save(new_animal_allergy)
    return redirect("/allergys")