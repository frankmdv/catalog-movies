from flask import Flask, redirect, render_template, request, url_for
from models import Film, Catalog

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        film_name = request.form['film-name']
        film_synopsis = request.form['film-synopsis']
        film_director = request.form['film-director']

        film = Film(film_name, film_synopsis, film_director)
        Catalog.add_film(film)


    return render_template('index.html', 
                           catalog_films = Catalog.fetch_catalog())

@app.route('/remove/<name>')
def remove(name):
    Catalog.remove_film(name)
    return redirect(url_for('index'))
