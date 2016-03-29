# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.babel import Babel
from flask.ext.mail import Mail

import config

login_manager = LoginManager()
db = SQLAlchemy()
mail = Mail()
babel = Babel()

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(user_id)


def create_app():
    from views import auth, user, home

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)

    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(home)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    babel.init_app(app)

    with app.app_context():
        db.create_all()

    return app


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app = create_app()

    @babel.localeselector
    def get_locale():
        try:
            l = session['locale']
        except KeyError:
            l = None
            session['locale'] = None
        if l is not None:
            return l
        else:
            return 'en'
    app.run()
