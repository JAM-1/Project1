from db.run_sql import run_sql
from models.allergy import Allergy

def save(allergy):
    sql = "INSERT INTO allergies (name) VALUES (%s) RETURNING *"
    values = [allergy.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    allergy.id = id
    return allergy

def select_all():
    animals = []
    sql = "SELECT * FROM allergies"
    results = run_sql(sql)
    for row in results:
        allergy = Allergy(row['name'], row['id'])
        animals.append(allergy)
    return animals

def select_all_id(id):
    animals = []
    sql = "SELECT * FROM allergies WHERE animal_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        allergy = Allergy(row['name'], row['id'])
        animals.append(allergy)
    return animals

def select(id):
    allergy = None
    sql = "SELECT * FROM allergies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        allergy = Allergy(result['name'], result['id'])
    return allergy

def delete(id):
    sql = "DELETE FROM allergies WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM allergies"
    run_sql(sql)

def update(allergy):
    sql = "UPDATE allergies SET name = %s WHERE id = %s"
    values = [allergy.name, allergy.id]
    run_sql(sql, values)