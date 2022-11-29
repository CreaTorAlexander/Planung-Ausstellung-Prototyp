
from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__, static_folder="static")

# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    message = "Hello, World"
    return render_template('index.html', message=message)


@app.route("/content")
def content():
    message = "Hello, World"
    return render_template('content.html', message=message)

# run the application
if __name__ == "__main__":
    app.run(debug=True)