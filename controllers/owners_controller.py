from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

owners_blueprint = Blueprint("owners", __name__)

# LIST OWNERS: ACTION
@owners_blueprint.route("/owners")
def list_owners():
    all_owners = owner_repository.select_all()
    return render_template("/owners/index.html", all_owners= all_owners)

# DELETE OWNER: ACTION
@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete(id):
    owner_repository.delete(id)
    return redirect("/owners")

# NEW OWNER: PRESENT FORM
@owners_blueprint.route("/owners/new")
def new_animal():
    return render_template("/owners/new.html")

# CREATE NEW OWNER: ACTION
@owners_blueprint.route("/owners", methods=['POST'])
def create_new_owner():
    name = request.form['name']
    contact = request.form['contact']
    postal_address = request.form['address']
    new_Owner = Owner(name, contact, postal_address, 0)
    owner_repository.save(new_Owner)
    return redirect("/owners")

# EDIT OWNER: FORM
@owners_blueprint.route("/owners/<id>/edit", methods=['POST'])
def edit(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner)

# UPDATE EDITED OWNER: ACTION
@owners_blueprint.route("/owners/<id>", methods=['POST'])
def update(id):
    name = request.form['name']
    contact = request.form['contact']
    address = request.form['address']
    balance = request.form['balance']
    owner = Owner(name, contact, address, balance, id)
    owner_repository.update(owner)
    return redirect("/owners")

# SHOW OWNER DATA: ACTION 
@owners_blueprint.route("/owners/<id>", methods=['GET'])
def view_owner(id):
    owner = owner_repository.select(id)
    all_animals = animal_repository.select_id_owner(id)
    return render_template("owners/results.html", owner=owner, all_animals=all_animals)