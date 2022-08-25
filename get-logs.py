#!/usr/bin/env python3

from datetime import date

from db.eshop import cursor
from db.mongo import db, mongo

def getCount(table):
  cursor.execute(f"SELECT count(*) as count FROM {table}")
  (count,) = cursor.fetchone()  

  return count

def saveLog(row):
  today = date.today().strftime("%Y-%m-%d")
  log = db.logs.find_one({ "date": today })

  row["date"] = today

  if log != None:
    db.logs.update_one({ "date": today }, { "$set": row })
  else:
    db.logs.insert_one(row)

def main():
  row = {}
  tables = [ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ]

  for table in tables:
    print(f"[+] Get {table} count")
    row[table] = getCount(table)

  cursor.close()

  print("[+] Save log on database")
  saveLog(row)

  mongo.close()

  print("[+] Done!")

if __name__ == "__main__":
  main()
