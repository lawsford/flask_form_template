import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_app.utils.forms import LoginForm
from flask_app.utils.tools import verify_pass
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/login", methods=["GET", "POST"])
def login():
    print('LAKAD MATATAAAAAAAAAG')
    form = LoginForm()
    user = form.user_id.data
    if form.validate_on_submit():
        if verify_pass(user, form.password.data):
            print('NORMALIN NORMALIN', url_for("index"))
            session.clear()
            session["user"] = user
            return redirect(url_for("index"))
        else:
            flash("Authentication failed", "danger")
    return render_template("auth/login.html", title="Login", form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_id


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view