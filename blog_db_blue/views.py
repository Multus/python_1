# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    flash,
    url_for,
    g,
    session,
)
from flask.ext.login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)
from forms import (
    NewUserFrm,
    NewPostFrm,
    EnterUserFrm
)
from models import User, Post
from app import db
from flask_babel import gettext


auth = Blueprint('auth', __name__, url_prefix='/auth')
user = Blueprint('user', __name__, url_prefix='/user')
home = Blueprint('home',__name__)

@home.route('/', methods=['GET', 'POST'])
def main():
    p = Post.query.filter_by(is_visible=True).all()
    return render_template('posts.html', posts=p)


@home.route('/locale', methods=['GET'])
def locale_change():
    loc = session['locale']
    if loc is None:
        loc = 'en'
    else:
        if loc == 'en':
            loc = 'ru'
        else:
            loc = 'en'
    session['locale'] = loc
    flash(gettext('The language is changed'))
    return redirect(url_for('.main'))


@home.route('/cleardb', methods=['GET'])
def cleardb():
    users = User.query.all()
    posts = Post.query.all()
    for post in posts:
        db.session.delete(post)
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return 'Success'

@user.route('/status-post', methods=['POST'])
@login_required
def StatusPost():
    pid = request.form['post_id']
    met = request.form['method']
    if met == 'show':
        status = True
    else:
        status = False
    Post.query.filter_by(id=pid).update({'is_visible': status})
    db.session.commit()
    return redirect(url_for('.myposts'))


@user.route('/myposts', methods=['GET'])
@login_required
def myposts():
    p = current_user.posts.all()
    return render_template('posts.html', posts=p)


@user.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost():
    if request.method == 'GET':
        frm = NewPostFrm()
    else:
        frm = NewPostFrm(request.form)
        if frm.validate():
            p = Post(user=current_user, **frm.data)
            db.session.add(p)
            db.session.commit()
            flash(gettext('Post is added'))
        else:
            flash(gettext('Validation problem'))
    return render_template('form.html', form=frm, action=url_for('.newpost'))


@user.route('/exit', methods=['GET'])
@login_required
def user_exit():
    logout_user()
    return redirect(url_for('home.main'))


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        frm = EnterUserFrm()
    else:
        frm = EnterUserFrm(request.form)
        u = User.query.filter_by(email=request.form['email']).first()
        if u and u.check_pswd(request.form['pswd']):
            login_user(u)
            return redirect(url_for('user.myposts'))
        else:
            flash(gettext('Invalid email or password'))
    return render_template('form.html', form=frm, action=url_for('.login'))


@auth.route('/newuser', methods=['GET', 'POST'])
def newuser():
    from flask_mail import Message
    from app import mail
    if request.method == 'GET':
        frm = NewUserFrm()
    else:
        frm = NewUserFrm(request.form)
        if frm.validate():
            u = User()
            frm.populate_obj(u)
            u.set_pswd(frm.pswd1.data)
            db.session.add(u)
            db.session.commit()
            flash('User is added')
            rec = []
            rec.append(frm.email.data)
            msg = Message(gettext("You have registered successfully"),
                  sender="danil3dpy@yandex.ru",
                  recipients=rec)
            msg.body = gettext("The registration in Danil blog is succesfull")
            mail.send(msg)
        else:
            flash('Validation problem')
    return render_template('form.html', form=frm, action=url_for('.newuser'))