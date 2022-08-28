from flask import render_template, redirect, session

from models.settings import getUserPassword, updateUsername, updatePassword
from utils.hashing import verify

class SettingsController:
  def get(self):
    if not session.get("username"):
      return redirect("/login")

    return render_template("settings.html", page="settings")

  def updateUsername(self, request):
    if not session.get("username"):
      return redirect("/login")

    errors = {}

    username = session.get("username")

    password    = request.form["password"] 
    newUsername = request.form["username"] 

    if not newUsername:
      errors["username"] = "Must not be empty"
    elif newUsername == username:
      errors["username"] = "Must not be the same as the old one"

    if not password:
      errors["password"] = "Must not be empty"

    if len(errors):
      return render_template("settings.html", username=newUsername, usernameErrors=errors)

    if not verify(password, getUserPassword(username)):
      errors["password"] = "Wrong password"

    if len(errors):
      return render_template("settings.html", username=newUsername, usernameErrors=errors)

    session["username"] = newUsername
    updateUsername(username, newUsername)

    return redirect("/")
  
  def updatePassword(self, request):
    if not session.get("username"):
      return redirect("/login")

    errors = {}

    username = session.get("username")

    oldPassword = request.form["oldPassword"] 
    newPassword = request.form["newPassword"]
    
    if not oldPassword:
      errors["oldPassword"] = "Must not be empty"

    if not newPassword:
      errors["newPassword"] = "Must not be empty"

    if len(errors):
      return render_template("settings.html", passwordErrors=errors)

    if not verify(oldPassword, getUserPassword(username)):
      errors["oldPassword"] = "Wrong password"

    if newPassword == oldPassword:
      errors["newPassword"] = "The new password is the same as the old one"

    if len(errors):
      return render_template("settings.html", passwordErrors=errors)

    updatePassword(username, newPassword)

    return redirect("/")
