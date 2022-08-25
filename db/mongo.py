import os
import pymongo

try:
  mongo = pymongo.MongoClient(
    host=os.getenv("DB_HOSTNAME"),
    port=27017,
    serverSelectionTimeoutMS=500
  )

  db = mongo.logs
  mongo.server_info()
  print("[+] Connected to mongo database")
except (Exception) as err:
  print("Failed to connect to mongodb", err)
  exit(1)
