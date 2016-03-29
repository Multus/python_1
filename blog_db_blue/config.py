# -*- coding: utf-8 -*-

DEBUG = True
SECRET_KEY = 'asdfsdfssf asf dsgsdg'

# Database settings:
SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = '465'
MAIL_USE_SSL = True
MAIL_USERNAME = 'danil3dpy@yandex.ru'
MAIL_PASSWORD = '123python'

LANGUAGES = {
    'en': 'English',
    'ru': u'Русский',
}
