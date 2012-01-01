from flask import Blueprint, session, render_template
bp = Blueprint('home', __name__)

@bp.route("/")
def show_home():
    # Getting out the username proves that you are logged in... ;)
    from mu.model.repository.user import fetch_user_with_uuid
    user = fetch_user_with_uuid(session['uuid'])

    return render_template("home.html", username=user.username)
