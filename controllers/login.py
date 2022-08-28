from flask import render_template, redirect, session

from models.login import getUser
from utils.hashing import verify

class LoginController:
  def get(self, request):
    if session.get("username"):
      return redirect("/")

    return render_template("login.html")

  def post(self, request):
    errors = {}

    username = request.form["username"] 
    password = request.form["password"] 

    user = getUser(username)

    if not username:
      errors["username"] = "Must not be empty"
    elif not user:
      errors["username"] = "User does not exist"

    if not password:
      errors["password"] = "Must not be empty"

    if len(errors):
      return render_template("login.html", username=username, errors=errors)

    if not verify(password, user["password"]):
      errors["password"] = "Wrong password"

    if len(errors):
      return render_template("login.html", username=username, errors=errors)

    session["username"] = username

    return redirect("/")

loginController = LoginController()
