from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
  blogs_data = [
    {"id":1,"title":"Blog 1", "content":"this is the blog 1"},
    {"id":2,"title":"Blog 2", "content":"this is the blog 2"},
    {"id":3,"title":"Blog 3", "content":"this is the blog 3"},
    {"id":4,"title":"Blog 4", "content":"this is the blog 4"},
    {"id":5,"title":"Blog 5", "content":"this is the blog 5"},
  ]

  return render_template("index.html", Blogs_data = blogs_data)

if __name__ == "__main__":
  app.run(debug=True)