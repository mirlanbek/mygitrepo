-------------------- templates-------- Coorey 2---------------------------------

mkdir templates
cd templates
touch about.html home.html layout.html

# Note: call template in flaskfile with render_template 
from flask import render_template

use:

@app.route("/home")
def home():
    return render_template("home.html")

-------------------------------- posts ----- list of dicts --------------------------
# dummy database

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

title = "This is external title"

We need pass this database 'posts' to template using 'url_for':

from flask import url_for

use:

@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title=title)

----------------- jinja2 template --------------

    {% if title %}
        <title>Flask Blog - {{ title }}</title>
    {% else %}
        <title>Flask Blog</title>
    {% endif %}


<body>

{% for post in posts %}
    <h1> {{ post.title }}
    <p1> By author {{ post.author }} on posted date {{  post.date_posted }} </p>
    <p> {{ post.content }} </p>
{% endfor %}

</body>

---------- Template inherit---------------------------------
vim layouts.html

<html>
<head>
</head>
<title> HOME PAGE </title>

<body>

{% block A %} {% endblock %}  # here

</body>
</html>

############################################################################

vi about.html
--

# import layout common file:
{% extends "layout.html" %}

{% block A %} #start

{% if posts %}
    {% for post in posts %}
        Salam {{ post.name }}
        Sen {{ post.age }} jashtasynby?

    {% endfor %}

{% endif %}
{% endblock A %} # end

######################################################



------------- first flask  file --- Coorey 1 ------------------------

from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/images")
def images():
    return "<img src='ll /home/mirlan/Downloads/html/alarm.jpg'width='80' height='150'>"


if __name__ == '__main__':
    app.run(debug=True)






------------ instalation----- ---------------------
pip install flask
import flask

run sever:

