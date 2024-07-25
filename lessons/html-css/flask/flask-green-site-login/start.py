from flask import Flask, flash, redirect, url_for, render_template, request, session
import time
from os import environ, path
from dotenv import load_dotenv
user=False

app = Flask(__name__)
app.config['SECRET_KEY'] = ' '


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, 'env'))




@app.route("/home",methods=['POST', 'GET'])
def home():
    if not user:
        return render_template('login.html', title='Login')
    else:
        return render_template("home.html", title="Home is best")


@app.route("/clients",methods=['POST'])
def clients():
    if not user:
        return render_template('login.html', title='Login')
    else:    
        return render_template("clients.html",title="Clients is best")



@app.route("/services",methods=['POST', 'GET'])
def services():
    if not user:
        return render_template('login.html', title='Login')
    else:
        return render_template("services.html",title="Services is best")



@app.route("/investors",methods=['POST', 'GET'])
def investors():
    if not user:
        return render_template('login.html', title='Login')
    else:
        return render_template("investors.html",title="Investors is best")



@app.route("/pricing",methods=['POST', 'GET'])
def pricing():
    if not user:
        return render_template('login.html', title='Login')
    else:    
        return render_template("pricing.html",title="Pricing is best")


@app.route("/training",methods=['POST', 'GET'])
def training():
    if not user:
        return render_template('login.html', title='Login')
    else:    
        return render_template("training.html",title="Training is best")



@app.route("/contact",methods=['POST', 'GET'])
def contact():
    # if session.get('username') is None or session.get('if_logged') is None:
    if not user:
        return render_template('login.html', title='Login')
    else:
        return render_template("contact.html",title="Contacts is best")




@app.route("/")
@app.route("/login", methods=['POST', 'GET'])
def login():
    # Output a message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL

        if username in environ["LOGIN"] and password in environ["PASS"]: 
        # if account:cd
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = environ["LOGIN"]

            global user
            user = environ["LOGIN"]
            # Redirect to home page

            flash('You have been logged in!', 'success')
            return redirect(url_for('home', title="Admin"))
        else:
            # Account doesnt exist or username/password incorrect
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login')
            


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
