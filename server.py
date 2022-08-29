#!/usr/bin/env python3

from flask import Flask, request, session, redirect
from flask_session import Session

from controllers.home import HomeController
from controllers.login import LoginController
from controllers.settings import SettingsController

app = Flask(__name__, static_url_path="/public", static_folder="/home/seif/projects/e-shop/seo-dashboard/public")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.get("/")
def index():
  if not session.get("username"):
    return redirect("/login")
  else:
    return HomeController(request).render()

@app.route("/settings", methods=[ "GET", "POST" ])
def settings():
  if not session.get("username"):
    return redirect("/login")
  else:
    return SettingsController(request).render()

@app.route("/login", methods=[ "GET", "POST" ])
def login():
  return LoginController(request).render()

@app.get("/logout")
def logout():
  session["username"] = None
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True, port=8080, host="0.0.0.0")
