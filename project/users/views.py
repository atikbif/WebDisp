#################
#### imports ####
#################
 
from flask import render_template, Blueprint,url_for,redirect,flash,session,request
from .forms import LoginForm
from ..models import User
from flask_login import login_user,login_required,current_user,logout_user


 
 
################
#### config ####
################
 
users_blueprint = Blueprint('users', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@users_blueprint.route('/',methods=('GET','POST'))
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        form.password.data=''
        user = User.query.filter_by(email = email).first()
        if user is not None:
            if user.check_password(password):
                user.authenticated = True
                login_user(user)
                session['email']=email
                return redirect(request.args.get('next') or url_for('object_list.obj_list'))
            else:
                flash("Некорректный пароль")
        else:
            flash("Почтовый ящик не зарегистрирован")
    #session['email'] = None
    #logout_user()
    return render_template('login.html',form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    session['email'] = None
    return redirect(url_for('users.login'))