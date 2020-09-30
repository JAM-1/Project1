DROP TABLE owners, vets, animals, medicals, allergies, animal_allergies;

CREATE TABLE owners ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact VARCHAR(255),
    address VARCHAR(255),
    balance FLOAT
);

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE animals ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    dob VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id)
);

CREATE TABLE medicals(
    id SERIAL PRIMARY KEY,
    description TEXT,
    animal_id INT REFERENCES animals(id)

);

CREATE TABLE allergies(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    
);

CREATE TABLE animal_allergies(
    id SERIAL PRIMARY KEY,
    animal_id INT REFERENCES animals(id),
    allergy_id INT REFERENCES allergies(id)
);
