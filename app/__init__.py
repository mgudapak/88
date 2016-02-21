from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config') # reads from config.py in root folder

@app.route('/')
def index():
    return "Hello Constellations!"

if __name__ == "__main__":
    app.run()
