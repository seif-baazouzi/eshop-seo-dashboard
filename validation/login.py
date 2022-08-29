from models.login import getUser
from utils.hashing import verify

def validateLogin(username, password):
  errors = {}
  user = getUser(username)

  if not username:
    errors["username"] = "Must not be empty"
  elif not user:
    errors["username"] = "User does not exist"

  if not password:
    errors["password"] = "Must not be empty"

  if len(errors):
    return errors

  if not verify(password, user["password"]):
    errors["password"] = "Wrong password"
  
  return errors
