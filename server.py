#!/usr/bin/env python3

from flask import Flask, request, session, redirect
from flask_session import Session

from controllers.home import homeController
from controllers.login import loginController
from controllers.settings import SettingsController

app = Flask(__name__, static_url_path="/public", static_folder="/home/seif/projects/e-shop/seo-dashboard/public")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.get("/")
def index():
  return homeController(request)

@app.route("/settings", methods=[ "GET", "POST" ])
def settings():
  queryParams = request.args.to_dict()

  if "form" in queryParams and request.method == "POST":
    form = queryParams["form"]

    if form == "update-username":
      return SettingsController().updateUsername(request)

    if form == "update-password":
      return SettingsController().updatePassword(request)

  return SettingsController().get()

@app.route("/login", methods=[ "GET", "POST" ])
def login():
  if request.method == "POST":
    return loginController.post(request)
  else:
    return loginController.get(request)

@app.get("/logout")
def logout():
  session["username"] = None
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True, port=8080, host="0.0.0.0")
