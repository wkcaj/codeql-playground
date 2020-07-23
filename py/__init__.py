from flask import Blueprint, request

import requests

bp = Blueprint('test', __name__, url_prefix='/abc')

@bp.route('/test')
def test():
    user_data = request.args.get('user')
    requests.get(user_data)

@bp.route('/test2')
def test2():
    user_data = request.args.get('user')
    print(user_data)

@bp.route('/test3')
def test3():
    requests.get("/")

@bp.route('/test4')
def test4():
    user_data = request.args['user']
    requests.get(user_data)
