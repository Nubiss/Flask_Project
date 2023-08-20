from app import app
from flask import render_template, request
from datetime import datetime
from.forms import UserNameForm

@app.route ('/', methods=['GET'])
@app.route('/index')
def index():
        form = UserNameForm()
        return render_template ("index.html", form = form);

@app.route('/info')
def info ():
        return render_template("info.html")

@app.route ('/', methods=['POST'])
@app.route ('/index', methods =['POST'])
def index_post():
#         text = request. form ['user_name']
        form = UserNameForm()
        if form.validate_on_submit():
                text1= form.UserNameField.data
                text2 = form.UserSurNameField.data
                text3 = form.UserEmailField.data
                return render_template ("index.html", form = form, user_name = text1, user_surname = text2, user_email = text3);
        else:
                return "Bad form"