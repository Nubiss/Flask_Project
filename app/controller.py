from app import app, model, repository
from flask import render_template, request
from datetime import datetime
from .forms import UserNameForm, CredentialsForm

@app.route('/register', methods=['GET'])
def register():
        form = CredentialsForm()
        return render_template ("register.html", form = form);
        
        
@app.route('/register', methods=['POST'])
def register_post():
        form = CredentialsForm()
        if form.validate_on_submit():
                credentials = model.Credentials(login = form.loginField.data, password = form.passwordField.data)
                if repository.checkLogin(credentials.login):
                        repository.saveCredentials (credentials)
                        return "Login acceptable"
                else:
                        return "Login exists"
        return render_template ("register.html", form = form);

@app.route ('/', methods=['GET'])
@app.route('/index')
def index():
        form = UserNameForm()
        formDelete = UserNameForm()
        roles = repository.getRoles()
        return render_template ("index.html", form = form, roles = roles, formDelete = formDelete);

@app.route('/info')
def info ():
        return render_template("info.html")

@app.route ('/', methods=['POST'])
@app.route ('/index', methods =['POST'])
def index_post():
#         text = request. form ['user_name']
        form = UserNameForm()
        if form.validate_on_submit():
                user1 = model.Users()
                user1.name = "Pavel"
                user1.surname = "Sirenski"
                user2 = model.Users()
                user2.name = "Ivan"
                user2.surname = "Ivanovsky"
                user3 = model.Users()
                user3.name = "Peter"
                user3.surname = "Petrovskij"
                users = [user1, user2, user3]
                
                service1 = model.Services()
                service1.service_type = "Project_Audit"
                service2 = model.Services()
                service2.service_type = "Corporate_Project_Management_Implementation"
                services = [service1, service2]
                
                payment1 = model.Payments()
                payment1.payment_type = "Prepayment_100%"
                payment2= model.Payments()
                payment2.payment_type = "Partial_Prepayment_50/50"
                payment3 = model.Payments()
                payment3.payment_type = "Postpayment_100%"
                payments = [payment1, payment2, payment3]
                
                text1 = form.UserNameField.data
                text2 = form.UserSurNameField.data
                text3 = form.UserEmailField.data
                
                
                repository.saveRole(text)
                roles = repository. getRoles()
                text = text
                return render_template ("index.html", form = form, user_name = text1, user_surname = text2, user_email = text3, users = users, services = services, payments = payments, roles = roles);
        else:
                return "Bad form"
        
@app.route ('/delete_role', methods =['POST'])
def delete_role():
        delete_id = request.args.get('delete_id')
        repository.deleteRole(delete_id)
        form = UserNameForm()
        roles = repository.getRoles()
        return render_template ("index.html", form = form, roles = roles);

@app.route ('/user')
def userInfo():
        return "User";
# Почему при запуске VS Code пишет ошибку: "ModuleNotFoundError: No module named 'app'"?
