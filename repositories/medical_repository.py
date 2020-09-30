from db.run_sql import run_sql
from models.medical import Medical


def save(medical):
    sql = "INSERT INTO medicals (description, animal_id) VALUES (%s, %s) RETURNING *"
    values = [medical.description, medical.animal_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    medical.id = id
    return medical

def delete_all():
    sql = "DELETE FROM medicals"
    run_sql(sql)

def select_all_med(id):
    history = []
    sql = "SELECT * FROM medicals WHERE animal_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        procedure = Medical(row['description'], row['id'])
        history.append(procedure)
    return history