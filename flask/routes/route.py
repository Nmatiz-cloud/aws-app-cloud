from server import app
from controllers.control import *

@app.route('/')
def home_page():
    return func_home_page()

@app.route('/register')
def register():
    return func_register()

@app.route('/consult_page')
def consult_page():
    return func_consult_page()

@app.route('/registro', methods=['post'])
def registro():
    return func_registro()

@app.route('/consult_user', methods=['post'])
def consult_user():
    print(request.get_json())
    return func_consult_user()
