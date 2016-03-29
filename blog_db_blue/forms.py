# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms_alchemy import model_form_factory
from wtforms import PasswordField, StringField
from flask.ext.babel import gettext

from models import User, Post

BaseForm = model_form_factory(Form)

class NewUserFrm(BaseForm):
    pswd1 = PasswordField(gettext('Password'))
    pswd2 = PasswordField(gettext('Repeat password'))
    class Meta:
        model = User
        only = ['username', 'email']

    def validate(self):
        super(NewUserFrm, self)
        if self.pswd1.data == self.pswd2.data:
            return True
        else:
            return False


class EnterUserFrm(BaseForm):
    pswd = PasswordField(gettext('Password'))
    class Meta:
        model = User
        only = ['email']


class NewPostFrm(BaseForm):
    class Meta:
        model = Post
        only = ['title', 'content']