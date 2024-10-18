from flask import Flask, render_template, request
from database.db import connectionsql, add_user 
from controllers.admin_s3 import *
from server import app

def func_home_page():
    return render_template("home.html")

def func_register():
    return render_template("register.html")

def func_registro():
#obtiene lista los objetos del bucket definido en el archivo admin_s3.py
    data_user = request.form
    data_photo = request.files
    ID = data_user["ID"]
    NAME_USER = data_user["NAME_USER"]
    LAST_NAME = data_user["LAST_NAME"]
    BIRTHDAY = data_user["BIRTHDAY"]
    ACT_LABORAL = data_user["ACT_LABORAL"]
    photo = data_photo["photo"]
    add_user(ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL)
    photo_path, photo_name = save_file(photo)
    upload_file(photo_path, photo_name)
    return "usuario añadido"

def func_consult_page():
    return render_template("consult.html")

def func_consult_user():
    return "OK"
