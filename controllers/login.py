from flask import render_template, redirect, session

from validation.login import validateLogin

class LoginController:
  def __init__(self, request):
    self.request = request
  
  def render(self):
    if self.request.method == "POST":
      return self.post()
    else:
      return self.get()

  def get(self):
    return render_template("login.html")

  def post(self):
    username = self.request.form["username"]
    password = self.request.form["password"]

    errors = validateLogin(username, password)
    if len(errors):
      return render_template("login.html", username=username, errors=errors)

    session["username"] = username

    return redirect("/")
