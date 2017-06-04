from flask import Flask, render_template

app = Flask(__name__)

# Set route to home page
@app.route("/")
def index():
  return render_template("index.html")

# Set route to about page
@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)