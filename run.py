#!/usr/local/bin/python

# File that is invoked to start up a development server.
# It gets a copy of the app from your package and runs it.
from app import app

if __name__ == "__main__":
    app.run(port=8000, debug=True)
