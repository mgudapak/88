# Application package constructor
from flask import Flask, render_template
from data.constellations import constellations

constellations = constellations
# constellation_data_files = constellation_data_files

print constellations
# print constellation_data_files

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')  # reads from config.py in root folder


@app.route('/')
def home_page():
    return render_template('index.html', constellations=constellations)
