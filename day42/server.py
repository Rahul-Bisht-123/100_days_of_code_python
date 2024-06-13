from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
  return '''
  <h1>Welcome to guess the gender and age Page.</h1>
  <h2>Go to url localhost:5000/guess/name</h2>
'''
         
@app.route("/guess/<user_name>")
def guess(user_name):

  gender_api = requests.get(f"https://api.genderize.io?name={user_name}").json()
  gender = gender_api["gender"]

  age_api = requests.get(f"https://api.agify.io?name={user_name}").json()
  age = age_api["age"]

  return render_template("index.html",Name=user_name.title() ,Gender=gender,Age=age)


if __name__ == "__main__":
  app.run(debug=True)
