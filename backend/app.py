from flask import Flask
from db import db
from dotenv import load_dotenv
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
    collections = db.list_collection_names()
    return f"Connected! Collections: {collections}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
