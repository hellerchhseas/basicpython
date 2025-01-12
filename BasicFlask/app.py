from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1> Adopt a Pet!</h1>
  <p> Browse through the links below to find your new furry friend: </p>
  <ul>
      <li><a href="/animals/dogs">Dogs</a></li>
      <li><a href="/animals/cats">Cats</a></li>
      <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1> List of {pet_type} </h1>'
  html += '<ul>'
  
  for index, pet in enumerate(pets[pet_type]):
      html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'
  
  html += '</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]

  # HTML RESPONSE variables
  pet_name = pet['name']
  pet_image = pet['url']
  pet_description = pet['description']
  pet_breed = pet['breed']
  pet_age = pet['age']

  # HTML RESPONSE CONSOLIDATION
  html = f'<h1>{pet_name}</h1>'
  html += f'<img src="{pet_image}" alt="Photo of {pet_name}" style="width:300px;height:auto;">'
  html += f'<p>{pet_description}</p>'
  html += '<ul>'
  html += f'<li>Breed: {pet_breed}</li>'
  html += f'<li>Age: {pet_age} years old</li>'
  html += '</ul>'

  return html
