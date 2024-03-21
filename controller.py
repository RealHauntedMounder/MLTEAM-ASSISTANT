from models import *
from flask import render_template, redirect, url_for, flash, Blueprint, request, jsonify, abort, current_app, session
from flask_admin.contrib.sqla import ModelView
from functools import wraps
from flask_login import login_user, login_required, current_user, logout_user
from config import create_app, bcrypt, babel, db
import requests, hashlib, json, random, secrets, datetime
from datetime import datetime
import uuid
import time

routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")



@routes.route("/")
def signup():
	return render_template("registration.html")

@routes.route("/signin")
def signin():
	return render_template("login.html")


@routes.route("/anketa")
def anketa():
	return render_template("anketa.html")