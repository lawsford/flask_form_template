from time import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_app.utils.forms import MainForm, LoginForm
from werkzeug.exceptions import abort

from flask_app.auth import login_required

bp = Blueprint('form', __name__)


@login_required
@bp.route('/', methods=["GET", "POST"])
def index():
    form = MainForm()
    if form.validate_on_submit():
        payload = {
            "id": form.mandatory_string_field.data,
            "gate": form.optional_string_field.data,
            "issued_at": int(time()),
        }
    return render_template("main/index.html", title="Create Token", form=form)