#!/usr/bin/env python3

from db.eshop import cursor

def getUsersCount():
  cursor.execute("SELECT count(*) as count FROM users")
  (usersCount,) = cursor.fetchone()  

  return usersCount

def getShopsCount():
  cursor.execute("SELECT count(*) as count FROM shops")
  (shopsCount,) = cursor.fetchone()  

  return shopsCount

print(f"[+] Users Count = {getUsersCount()}")
print(f"[+] Shops Count = {getShopsCount()}")
