
#web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("You visited the homepage")
    #return f"Hello, World!"
    return render_template("prediction_form.html")
@home_routes.route("/about")
def about():
    print("You visited the about page")
    return f"About Me (TODO)!"