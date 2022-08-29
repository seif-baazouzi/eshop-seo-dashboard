from flask import render_template, redirect, session

from utils.hashing import verify
from models.settings import updateUsername, updatePassword
from validation.settings import validateUpdateUsername, validateUpdatePassword

class SettingsController:
  def __init__(self, request):
    self.request = request

  def render(self):
    queryParams = self.request.args.to_dict()

    if "form" in queryParams and self.request.method == "POST":
      form = queryParams["form"]

      if form == "update-username":
        return self.updateUsername()

      if form == "update-password":
        return self.updatePassword()

    return self.get()

  def get(self):
    if not session.get("username"):
      return redirect("/login")

    return render_template("settings.html", page="settings")

  def updateUsername(self):
    username = session.get("username")
    password    = self.request.form["password"] 
    newUsername = self.request.form["username"] 

    errors = validateUpdateUsername(username, newUsername, password)
    if len(errors):
      return render_template("settings.html", username=newUsername, usernameErrors=errors)

    session["username"] = newUsername
    updateUsername(username, newUsername)

    return redirect("/")
  
  def updatePassword(self):
    username = session.get("username")

    oldPassword = self.request.form["oldPassword"] 
    newPassword = self.request.form["newPassword"]

    errors = validateUpdatePassword(username, oldPassword, newPassword)
    if len(errors):
      return render_template("settings.html", passwordErrors=errors)

    updatePassword(username, newPassword)

    return redirect("/")
