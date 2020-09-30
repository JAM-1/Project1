from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(vet):
    sql = "INSERT INTO vets (name, contact) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['contact'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        vet = Vet(results['name'], results['contact'], results['id'])
    return vet

def update(vet):
    sql = "UPDATE vets SET (name, contact) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.contact, vet.id]
    run_sql(sql, values)