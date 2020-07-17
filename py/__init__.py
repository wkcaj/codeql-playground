from flask import Blueprint, request

import requests

bp = Blueprint('test', __name__, url_prefix='/abc')

@bp.route('/test')
def test():
    user_data = request.args.get('user')
    requests.get(user_data)