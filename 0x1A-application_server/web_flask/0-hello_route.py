from flask import Flask

# create an instance of flask
app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=True)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(port=5000)
