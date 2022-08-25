#!/usr/bin/env python3

from db.eshop import cursor

def getUsersCount():
  cursor.execute("SELECT count(*) as count FROM users")
  (usersCount,) = cursor.fetchone()  

  return usersCount

print(f"[+] Users Count = {getUsersCount()}")
