from flask import Flask, render_template , session , request, url_for, g, request, redirect ,flash,send_from_directory
from database import get_db,close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps 

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"]= "this-isn't-my-secret-key"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
