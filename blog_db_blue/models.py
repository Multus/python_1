# -*- coding: utf-8 -*-

from app import db
from datetime import datetime, date
from wtforms.validators import Email
from flask.ext.babel import gettext
import qrcode
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from wtforms import widgets
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(80), info={'label': gettext('Name')})
    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
        index=True,
        info={
            'validators': Email(),
            'label': u'Эл. почта'
        }
    )
    pswd = db.Column(db.String(200), nullable=False, info={'label': gettext('Password')})

    def set_pswd(self, pswd):
        self.pswd = generate_password_hash(pswd)

    def check_pswd(self, pswd):
        return check_password_hash(self.pswd, pswd)

    def __repr__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    user = db.relationship(
        'User', backref=db.backref('posts', lazy='dynamic')
    )

    title = db.Column(db.String(140), unique=True, info={'label': gettext('Title')})
    content = db.Column(db.String(3000), info={'label': gettext('Content'), 'widget': widgets.TextArea()})
    date_created = db.Column(db.Date, default=date.today())
    is_visible = db.Column(db.Boolean, default=True)
    qr_path = db.Column(db.String(200))

    def __init__(self, title='', content='', user=None,
                 date_created=None, is_visible=None):
        self.title = title
        self.content = content
        self.user = user

        path = datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.png'
        self.qr_create(title, path)
        self.qr_path = path

        if date_created is not None:
            self.date_created = date_created

        if is_visible is not None:
            self.is_visible = is_visible

    def qr_create(self, to_qr, fname):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(to_qr)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('static/' + fname)
