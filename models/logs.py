from db.mongo import db

def getLastLog():
  log = list(db.logs.find().sort("date", -1).limit(1))
  
  if len(log) > 0:
    return log[0]
  
  return None
