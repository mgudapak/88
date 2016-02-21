# File that is invoked to start up a development server.
# It gets a copy of the app from your package and runs it.

from app import app
app.run(debug=True)