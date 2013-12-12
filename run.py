#!/home/kevin/.virtualenvs/flaskblog/bin/python
#TODO: cleaner way to make above path?

# Simple init script to run the basic Flask server
from app import app
app.run(debug=True)
