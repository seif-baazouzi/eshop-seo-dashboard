from db.mongo import db

def getLastLog():
  log = list(db.logs.find().sort("date", -1).limit(1))
  
  if len(log) > 0:
    return log[0]
  
  return None

def getMonthLogs(month):
  startingDate = f"{month}-01"
  endingDate   = f"{month}-31"

  logs = list(db.logs.find({ "date": { "$gte": startingDate, "$lte": endingDate } }))

  return logs
