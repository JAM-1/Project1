from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository


def save(animal):
    sql = "INSERT INTO animals (name, type, dob, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.dob, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['type'], row['dob'], owner, vet, row['id'])
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['type'], result['dob'], owner, vet, result['id'])
    return animal

def select_id(id):
    animals = []
    sql = "SELECT * FROM animals WHERE vet_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['type'], row['dob'], owner, vet, row['id'])
        animals.append(animal)
    return animals

def select_id_owner(id):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['type'], row['dob'], owner, vet, row['id'])
        animals.append(animal)
    return animals

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def update(animal):
    sql = "UPDATE animals SET (name, type, dob, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.type, animal.dob, animal.owner.id, animal.vet.id, animal.id]
    run_sql(sql, values)