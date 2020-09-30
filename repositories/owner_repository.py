from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet


def save(owner):
    sql = "INSERT INTO owners (name, contact, address, balance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.contact, owner.address, owner.balance]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        owner = Owner(results['name'], results['contact'], results['address'], results['balance'], results['id'])
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['contact'], row['address'], row['balance'], row['id'])
        owners.append(owner)
    return owners

def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name, contact, address, balance) = (%s,%s,%s,%s) WHERE id = %s"
    values = [owner.name, owner.contact, owner.address, owner.balance, owner.id]
    run_sql(sql, values)