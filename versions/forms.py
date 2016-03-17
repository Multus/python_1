# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, validators, ValidationError

def full_name_validator(form, field):
    name_parts = field.data.split(' ')
    if len(name_parts) < 2:
        raise ValidationError('Name is not full!')

class v(Form):
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email(),
    ])
    ])
    version = Boolean(label='version')

class v1(v):
    name = StringField(label='Name', validators=[
        validators.Length(min=2, max=100), full_name_validator,
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email(),
    ])

class v2(v):
    name = StringField(label='Name', validators=[
        validators.Length(min=2, max=100),
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email(),
    ])