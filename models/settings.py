from db.mongo import db
from utils.hashing import hash

def getUserPassword(username):
  users = list(db.users.find({ "username": username }, { "password": 1, "_id": -1 }))
  return users[0]["password"]

def updateUsername(username, newUsername):
  db.users.update_one({ "username": username }, { "$set": { "username": newUsername } })

def updatePassword(username, password):
  passwordHash = hash(password) 
  db.users.update_one({ "username": username }, { "$set": { "password": passwordHash } })
