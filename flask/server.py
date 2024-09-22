from flask import Flask, render_template, request
from database.db import connectionsql, add_user 

app= Flask(__name__)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/registro', methods=['post'])
def registro():
    data_user = request.form
    ID = data_user["ID"]
    NAME_USER = data_user["NAME_USER"]
    LAST_NAME = data_user["LAST_NAME"]
    BIRTHDAY = data_user["BIRTHDAY"]
    ACT_LABORAL = data_user["ACT_LABORAL"]
    print(data_user)
    add_user(ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL)
    return "usuario añadido"

if __name__ == "__main__":
    ip = "172.31.28.123"
    port = "80"
    app.run(ip, port)