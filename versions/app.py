# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

from course7.flask.with_templates import config
from course7.flask.with_templates import Forms

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = ContactForm(request.form)
        form.validate()
    else:
        form = ContactForm()
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run()
