from flask_login import login_manager
import flask_login
from __init__ import login_manager

#initial user
users = {'admin@gmail.com': {'password': 'admin123'}}

class User(flask_login.UserMixin):
    @login_manager.user_loader
    def user_loader(email):
        if email not in users:
            return
        user = User()
        user.id = email
        return user


    @login_manager.request_loader
    def request_loader(request):
        email = request.form.get('email')
        if email not in users:
            return
        user = User()
        user.id = email
        user.is_authenticated = request.form['password'] == users[email]['password']
        return user

    # @login_manager.unauthorized_handler
    # def unauthorized_handler(self):
    #     return 'Unauthorized'