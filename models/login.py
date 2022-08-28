from db.mongo import db

def getUser(username):
  users = list(db.users.find({ "username": username }))
  
  if len(users) == 0:
    return False
  
  return users[0]
