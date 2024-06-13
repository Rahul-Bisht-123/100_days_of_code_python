from flask import Flask,render_template
import datetime

app = Flask(__name__)


@app.route("/")
def home():
  current_time = datetime.datetime.now()
  year = current_time.year

  return render_template("index.html" , name = "lion" , year = year)

if __name__ == "__main__":
  app.run(debug=True)