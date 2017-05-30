from flask import Blueprint

epicenter = Blueprint('epicenter', __name__)

from wdsauth.epicenter import views
