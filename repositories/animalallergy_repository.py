from db.run_sql import run_sql
from models.allergy import Allergy
from models.animal_allergy import AnimalAllergy
import repositories.animal_repository as animal_repository
import repositories.allergy_repository as allergy_repository


def save(animalallergy):
    sql = "INSERT INTO animal_allergies (animal_id, allergy_id) VALUES (%s, %s) RETURNING *"
    values = [animalallergy.animal_id.id, animalallergy.allergy_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animalallergy.id = id
    return animalallergy

def select_all():
    aallergy = []
    sql = "SELECT * FROM animal_allergies"
    results = run_sql(sql)
    for row in results:
        animal = animal_repository.select(row['owner_id'])
        allergy = allergy_repository.select(row['vet_id'])
        animalallergy = AnimalAllergy(row[animal], row[allergy])
        aallergy.append(animalallergy)
    return aallergy

def select(id):
    aallergy = None
    sql = "SELECT * FROM animal_allergies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        animal = animal_repository.select(result['owner_id'])
        allergy = allergy_repository.select(result['vet_id'])
        animalallergy = AnimalAllergy(result[animal], result[allergy])
        aallergy.append(animalallergy)
    return aallergy

def delete(id):
    sql = "DELETE FROM animal_allergies WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM animal_allergies"
    run_sql(sql)

def update(aallergy):
    sql = "UPDATE animal_allergies SET (animal_id, allergy_id) = (%s, %s) WHERE id = %s"
    values = [aallergy.animal.id, aallergy.allergy.id]
    run_sql(sql, values)


def select_all_id(id):
    allergies = []
    sql = "SELECT * FROM allergies INNER JOIN animal_allergies ON animal_allergies.allergy_id = allergies.id WHERE animal_allergies.animal_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        allergy = Allergy(row['name'])
        allergies.append(allergy)
    return allergies

