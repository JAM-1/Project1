import pdb

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.medical import Medical
from models.allergy import Allergy
from models.animal_allergy import AnimalAllergy

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.medical_repository as medical_repository
import repositories.allergy_repository as allergy_repository
import repositories.animalallergy_repository as animalallergy_repository


animal_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()
medical_repository.delete_all()
allergy_repository.delete_all()
animalallergy_repository.delete_all()



owner = Owner("Stephen Millington", "0141-123-4567", "Glasgow", 0.00)
owner1 = Owner("Tasnia Kaufman", "0131-098-7654", "Edinburgh", 0.00)
owner2 = Owner("Jo Bonner", "0777-666-5555", "Glasgow", 10.00)
owner3 = Owner("Dylon Kent", "0712-456-789", "Paisley", 0)
owner_repository.save(owner)
owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)


vet = Vet("Dr Smith", "07042650583")
vet1 = Vet("Dr Jones", "07818800317")
vet2 = Vet("Dr Sundance", "07055053958")
vet3 = Vet("Dr Butch", "07971728291")
vet_repository.save(vet)
vet_repository.save(vet1)
vet_repository.save(vet2)
vet_repository.save(vet3)


animal = Animal("Rover", "Dog", "2018", owner, vet)
animal1 = Animal("Tom", "Cat", "2017", owner1, vet1)
animal2 = Animal("Jerry", "Mouse", "2019", owner2, vet2)
animal3 = Animal("Nelly", "Elephant", "2019", owner3, vet3)
animal_repository.save(animal)
animal_repository.save(animal1)
animal_repository.save(animal2)
animal_repository.save(animal3)


med = Medical("Fleas", animal)
med1 = Medical("Anger Issues", animal1)
med3 = Medical("Work Place Stress", animal2)
med2 = Medical("Mouse Phobia", animal3)
medical_repository.save(med)
medical_repository.save(med1)
medical_repository.save(med2)
medical_repository.save(med3)

allergy = Allergy("Hayfever")
allergy1 = Allergy("Chocolate")
allergy2 = Allergy("Cat hair")
allergy_repository.save(allergy)
allergy_repository.save(allergy1)
allergy_repository.save(allergy2)

animalleg = AnimalAllergy(animal1, allergy)
animalleg1 = AnimalAllergy(animal1, allergy1)
animalleg2 = AnimalAllergy(animal2, allergy2)
animalallergy_repository.save(animalleg)
animalallergy_repository.save(animalleg1)
animalallergy_repository.save(animalleg2)