from flask import Blueprint

main = Blueprint('main', __name__)

from wdsauth.main import views, errors
