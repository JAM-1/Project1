from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.medical import Medical
import repositories.medical_repository as medical_repository
import repositories.animal_repository as animal_repository

medicals_blueprint = Blueprint("medicals", __name__)

# LIST
@medicals_blueprint.route("/medicals")
def animals():
    all_animals = animal_repository.select_all()
    return render_template("/medicals/index.html", all_animals= all_animals)

# CREATE NEW ANIMAL ACTION
@medicals_blueprint.route("/medicals", methods=['POST'])
def create():
    description = request.form['description']
    animal_id = request.form['animal']
    animal = animal_repository.select(animal_id)
    new_note = Medical(description, animal)
    medical_repository.save(new_note)
    return redirect("/medicals")