from flask import Flask
app = Flask(__name__)

def bold_Text(func):
  def wrapper(*args , **kwargs):
    result = func(*args , **kwargs)
    return f'<b>{result}</b>'
  return wrapper

def emp_Text(func):
  def wrapper(*args , **kwargs):
    result = func(*args , **kwargs)
    return f"<emp>{result}<emp>"
  return wrapper

def italic_Text(func):
  def wrapper(*args , **kwargs):
    result = func(*args , **kwargs)
    return f"<i>{result}<i>"
  return wrapper

  

@app.route("/")
@bold_Text
@italic_Text
@emp_Text
def home():
  return "Welcome to the Home Page"


if __name__ == "__main__":
  app.run(debug=True)    