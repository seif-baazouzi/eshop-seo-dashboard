from datetime import datetime

from db.mongo import db

def getLastLog():
  log = list(db.logs.find().sort("date", -1).limit(1))
  
  if len(log) > 0:
    return log[0]
  
  return None

def getMonthLogs():
  today = datetime.now()

  startingDate = f"01-{today.month}-${today.year}"
  endingDate   = f"31-{today.month}-${today.year}"

  logs = list(db.logs.find({ "date": { "$gte": startingDate, "$lte": endingDate } }))

  return logs
