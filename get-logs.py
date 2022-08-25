#!/usr/bin/env python3

from db.eshop import cursor

def getCount(table):
  cursor.execute(f"SELECT count(*) as count FROM {table}")
  (count,) = cursor.fetchone()  

  return count

print(f"[+] Users = {getCount('users')}")
print(f"[+] Shops = {getCount('shops')}")
print(f"[+] Items = {getCount('items')}")
print(f"[+] Carts = {getCount('carts')}")
print(f"[+] Comments = {getCount('itemsComments')}")
print(f"[+] Shops Rates = {getCount('shopsRates')}")
print(f"[+] Items Rates = {getCount('itemsRates')}")
