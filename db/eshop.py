import os
import sys
import psycopg2

database = os.environ["ESHOP_DATABASE"]
username = os.environ["ESHOP_USERNAME"]
password = os.environ["ESHOP_PASSWORD"]
hostname = os.environ["ESHOP_HOSTNAME"]

try:
  connection = psycopg2.connect(database=database, user=username, password=password, host=hostname, port=5432)
  cursor = connection.cursor()
  print("[+] Connected to eshop database")
except (psycopg2.DatabaseError) as err:
  print("Error on connection to the eshop database", err)
  sys.exit(1)
