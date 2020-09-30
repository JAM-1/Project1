from flask import Flask, render_template
app = Flask(__name__)

from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.allergies_controller import allergy_blueprint
from controllers.medicals_controller import medicals_blueprint
from controllers.allergys_controller import allergys_blueprint

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(allergy_blueprint)
app.register_blueprint(medicals_blueprint)
app.register_blueprint(allergys_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)