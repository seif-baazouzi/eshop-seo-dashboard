from utils.hashing import verify
from models.settings import getUserPassword

def validateUpdateUsername(username, newUsername, password):
  errors = {}

  if not newUsername:
    errors["username"] = "Must not be empty"
  elif newUsername == username:
    errors["username"] = "Must not be the same as the old one"

  if not password:
    errors["password"] = "Must not be empty"

  if len(errors):
    return errors

  if not verify(password, getUserPassword(username)):
    errors["password"] = "Wrong password"

  return errors

def validateUpdatePassword(username, oldPassword, newPassword):
  errors = {}

  if not oldPassword:
    errors["oldPassword"] = "Must not be empty"

  if not newPassword:
    errors["newPassword"] = "Must not be empty"

  if len(errors):
    return errors

  if not verify(oldPassword, getUserPassword(username)):
    errors["oldPassword"] = "Wrong password"

  if newPassword == oldPassword:
    errors["newPassword"] = "The new password is the same as the old one"

  return errors