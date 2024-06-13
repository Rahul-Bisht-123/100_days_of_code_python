from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Home Page<h1>"

@app.route("/about")
def about():
  return "<h1>About Page<h1>"

@app.route("/greet/<name>/<int:age>")
def greet(name,age):
  return f'''
  <h1>Welcome {name}. You are {age} years old</h1>
  <p>This is a Para</p>
  <span>This is a span</span>
  '''

if __name__ == "__main__":
  app.run(debug=True)