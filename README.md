# Project1

To run the code found in this repo:
(please note the following instructions are based on using a setup as per the original)
1. Clone repo.
  To clone this repo please follow the instructions found in the github.com link: 
  https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository

2. Download and install Flask (Python) or any other suitable web application framework.
3. Download and install PostgreSQL or any other suitable relational database management system
4. Open terminal and create a local SQL Database named 'vet_management' - Run the command: createdb vet_management
5. Open terminal and navigate to the location the repo was downloaded to, ensure you are at the same level as the app.py file.
6. Run the command: psql -d vet_management -f db/vet_management.sql
7. Run the command: python3 consoles.py
8. Run the command: Flask run
9. Open your browser (Google Chrome Version 85.0.4183.121 (Official Build) (64-bit)) and navigate to Localhost:5000

You should be presented with the Vet Surgery Management System welcome page.





The Project Brief:

Vet Management App

A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.
MVP

    The practice wants to be able to register / track animals. Important information for the vets to know is -
        Name
        Date Of Birth (use a VARCHAR initially)
        Type of animal
        Contact details for the owner
        Treatment notes
    Be able to assign animals to vets
    CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

Possible Extensions

    Mark owners as being registered/unregistered with the Vet. unregistered owners won't be able to add any more animals.
    If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have many pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)
    Handle check-in / check-out dates
    Let the practice see all animals currently in the practice (today's date is between the check-in and check-out?)
    Sometimes an owner does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 yr old dog is now 4.
    Add extra functionality of your choosing - assigning treatments, a more comprehensive way of maintaining treatment notes over time. Appointments. Pricing / billing.
    
    

Technologies and Tools used: 

    Visual Studio Code
    Flask (inc Blueprint extension)
    Google Chrome Browser
    Python
    PostgreSQL
    HTML
    CSS
    
