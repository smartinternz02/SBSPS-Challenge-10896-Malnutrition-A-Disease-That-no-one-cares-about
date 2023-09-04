from flask import Flask, request, render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/services")
def services_and_features():
    return render_template("services-details.html")
@app.route("/pictures")
def pictures():
    return render_template("portfolio-details.html")

if __name__ == "__main__":
    app.run(debug=True)